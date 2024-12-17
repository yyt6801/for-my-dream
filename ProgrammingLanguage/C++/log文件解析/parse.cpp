#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <utility>

void parse_log(const std::string& file_path, const std::string& target_pid, 
               std::vector<std::vector<std::pair<std::string, std::string>>>& parsed_results) {
    std::ifstream file(file_path);
    if (!file.is_open()) {
        std::cerr << "无法打开文件: " << file_path << std::endl;
        return;
    }

    std::vector<std::string> latest_data;
    std::string line;
    bool found_target = false;

    // 反向读取文件行
    std::vector<std::string> lines;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }
    file.close();

    // 从后往前查找
    for (auto it = lines.rbegin(); it != lines.rend(); ++it) {
        if (it->find("ProfPt: " + target_pid) != std::string::npos) {
            found_target = true;
            continue;
        }

        if (found_target && it->rfind("PRE", 0) == 0) {
            latest_data.push_back(*it);
            if (latest_data.size() == 8) { // 包括字段名行和7行数据
                break;
            }
        }
    }

    // 手动反转以恢复原始顺序
    std::vector<std::string> reversed_data;
    for (size_t i = latest_data.size(); i > 0; --i) {
        reversed_data.push_back(latest_data[i - 1]);
    }
    latest_data = reversed_data;

    // 解析字段名行
    std::vector<std::string> headers;
    std::stringstream header_stream(latest_data[0]);
    std::string header;

    // 使用空格分割字段名行
    while (header_stream >> header) { // 直接使用流提取操作符
        if (!header.empty()) {
            headers.push_back(header);
        }
    }

    // 解析数据行
    for (size_t i = 1; i < latest_data.size(); ++i) {
        std::vector<std::pair<std::string, std::string>> result; // 使用 vector 和 pair
        std::stringstream data_stream(latest_data[i]);
        std::string data;
        size_t index = 0;

        while (data_stream >> data) { // 直接使用流提取操作符
            if (!data.empty() && index < headers.size()) {
                result.push_back(std::make_pair(headers[index], data)); // 存储为 pair
                index++;
            }
        }

        if (index == headers.size()) {
            parsed_results.push_back(result);
        } else {
            std::cerr << "警告: 数据行与字段名长度不匹配: " << latest_data[i] << std::endl;
        }
    }
}

int main() {
    // std::string file_path = "c:\\Users\\Yuan\\Desktop\\PreRG-240812.log";
    std::string file_path = "PreRG-240812.log";
    std::string target_pid = "X24814903300";
    std::vector<std::vector<std::pair<std::string, std::string>>> parsed_results;

    parse_log(file_path, target_pid, parsed_results);

    // 访问特定行的字段
    if (!parsed_results.empty()) {
        // 访问第1行的 'Eprof' 字段
        for (const auto& pair : parsed_results[0]) {
            if (pair.first == "Eprof") {
                std::cout << "parsed_results[0][Eprof] = " << pair.second << std::endl;
            }
        }

        // 访问第2行的 'Pa' 字段（假设有第二行数据）
        if (parsed_results.size() > 1) {
            for (const auto& pair : parsed_results[1]) {
                if (pair.first == "Pa") {
                    std::cout << "parsed_results[1][Pa]=" << pair.second << std::endl;
                }
            }
        }
    }

    return 0;
}