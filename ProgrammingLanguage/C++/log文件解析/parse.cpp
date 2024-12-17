#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <utility>

int main() {
    std::string file_path = "PreRG-240812.log";
    std::string target_pid = "X24814903300";
    std::vector<std::vector<std::pair<std::string, std::string>>> parsed_results;

    std::ifstream file(file_path);
    if (!file.is_open()) {
        std::cerr << "无法打开文件: " << file_path << std::endl;
        return 1; // 添加返回值以指示错误
    }

    std::vector<std::string> lines;
    std::string line;

    // 读取文件行
    while (std::getline(file, line)) {
        lines.push_back(line);
    }
    file.close();

    // 从后往前查找最后一个 ProfPt:
    bool found_target = false;
    size_t target_index = 0;

    for (std::vector<std::string>::reverse_iterator it = lines.rbegin(); it != lines.rend(); ++it) {
        if (it->find("ProfPt: " + target_pid) != std::string::npos) {
            found_target = true;
            target_index = lines.size() - (it - lines.rbegin()) - 1; // 记录 ProfPt: 行的索引
            break; // 找到最后一个 ProfPt: 后退出循环
        }
    }

    // 如果找到了目标，读取该行后面的数据段
    if (found_target) {
        // 读取字段名行
        if (target_index + 1 < lines.size()) {
            std::string header_line = lines[target_index + 1];
            std::vector<std::string> headers;
            std::stringstream header_stream(header_line);
            std::string header;

            // 使用空格分割字段名行
            while (header_stream >> header) {
                if (!header.empty()) {
                    headers.push_back(header);
                }
            }

            // 读取数据行
            for (size_t j = target_index + 2; j < lines.size(); ++j) {
                if (lines[j].find(target_pid) != std::string::npos) { // 只处理与 target_pid 相关的行
                    std::vector<std::pair<std::string, std::string>> result; // 使用 vector 和 pair
                    std::stringstream data_stream(lines[j]);
                    std::string data;
                    size_t index = 0;

                    while (data_stream >> data) {
                        if (!data.empty() && index < headers.size()) {
                            std::pair<std::string, std::string> p(headers[index], data); // 使用 std::pair 的构造函数
                            result.push_back(p); // 存储为 pair
                            index++;
                        }
                    }

                    if (index == headers.size()) {
                        parsed_results.push_back(result);
                    } else {
                        std::cerr << "警告: 数据行与字段名长度不匹配: " << lines[j] << std::endl;
                    }
                }
            }
        }
    } else {
        std::cerr << "未找到目标 ProfPt: " << target_pid << std::endl;
    }

    // // 输出结果
    // for (size_t i = 0; i < parsed_results.size(); ++i) {
    //     std::cout << "Data from line " << i + 1 << ": ";
    //     for (size_t j = 0; j < parsed_results[i].size(); ++j) {
    //         std::cout << parsed_results[i][j].first << " = " << parsed_results[i][j].second << " ";
    //     }
    //     std::cout << std::endl;
    // }

    
    // 访问特定行的字段
    if (!parsed_results.empty()) {
        // 访问第1行的 'Eprof' 字段
        for (size_t i = 0; i < parsed_results[0].size(); ++i) {
            if (parsed_results[0][i].first == "Eprof") {
                std::cout << "parsed_results[0][Eprof] = " << parsed_results[0][i].second << std::endl;
            }
        }

        // 访问第2行的 'Pa' 字段（假设有第二行数据）
        if (parsed_results.size() > 1) {
            for (size_t i = 0; i < parsed_results[6].size(); ++i) {
                if (parsed_results[6][i].first == "Eprof") {
                    std::cout << "parsed_results[6][Eprof]=" << parsed_results[6][i].second << std::endl;
                }
            }
        }
    }

    return 0;
}