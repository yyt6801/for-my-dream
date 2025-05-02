#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>

int main() {
    std::string filePath = "EngLog-241219.log"; // 日志文件路径
    std::string targetID = "24C110544";
    // ParsedData result = parseLogFile(filePath, targetID);

    struct ParsedData {
    std::string MATNO;
    std::vector<std::string> CRT;
    std::vector<std::string> WEAR;
    };

    std::ifstream file(filePath.c_str()); // 使用 c_str() 以兼容旧版
    std::string line;
    ParsedData result;

    if (!file.is_open()) {
        std::cerr << "无法打开文件: " << filePath << std::endl;
    }

    std::vector<std::string> lines;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }
    file.close();

    // 反向查找最后一个包含目标卷号的行
    int targetIndex = -1;
    for (int i = lines.size() - 1; i >= 0; --i) {
        if (lines[i].find("ID") == 0 && lines[i].find(targetID) != std::string::npos) {
            targetIndex = i; // 记录目标卷号行的索引
            // 提取MATNO
            std::istringstream iss(lines[i + 1]);
            std::vector<std::string> fields;
            std::string field; // 在这里声明 field
            while (iss >> field) {
                fields.push_back(field);
            }
            result.MATNO = fields[7]; // MATNO在第8列（索引7）
            break;
        }
    }

    // 如果没有找到目标卷号，返回空结构
    if (targetIndex == -1) {
        std::cout << "没有找到目标卷号" << std::endl;
    }

    // 从找到的目标卷号行开始查找以P开头的行
    for (size_t j = targetIndex + 3; j < lines.size(); ++j) {
        if (lines[j].find("P") == 0) {
            // 提取CRT和WEAR字段名
            std::istringstream iss(lines[j]);
            std::vector<std::string> fieldNames;
            std::string field; // 在这里声明 field
            while (iss >> field) {
                fieldNames.push_back(field);
            }
            int crtIndex = std::find(fieldNames.begin(), fieldNames.end(), "CRT") - fieldNames.begin();
            int wearIndex = std::find(fieldNames.begin(), fieldNames.end(), "WEAR") - fieldNames.begin();

            // 提取机架数据
            for (size_t k = j + 2; k < j + 9 && k < lines.size(); ++k) {
                if (!lines[k].empty()) {
                    std::istringstream issData(lines[k]);
                    std::vector<std::string> values;
                    while (issData >> field) { // 在这里声明 field
                        values.push_back(field);
                    }
                    result.CRT.push_back(values[crtIndex]);
                    result.WEAR.push_back(values[wearIndex]);
                }
            }
            break;
        }
    }


    if (!result.MATNO.empty()) {
        std::cout << "MATNO: " << result.MATNO << std::endl;
        std::cout << "CRT: ";
        for (size_t i = 0; i < result.CRT.size(); ++i) {
            std::cout << result.CRT[i] << " ";
        }
        std::cout << std::endl;
        std::cout << "WEAR: ";
        for (size_t i = 0; i < result.WEAR.size(); ++i) {
            std::cout << result.WEAR[i] << " ";
        }
        std::cout << std::endl;
    } else {
        std::cout << "未找到指定卷号的数据。" << std::endl;
    }

    return 0;
}