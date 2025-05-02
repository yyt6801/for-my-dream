#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <regex>

struct RollData {
    std::string matNo;
    std::vector<std::pair<std::string, std::string>> crtWearData; // 存储 CRT 和 WEAR 数据
};

bool starts_with(const std::string& str, const std::string& prefix) {
    return str.substr(0, prefix.size()) == prefix;
}

int main() {
    std::ifstream file("RollData-240812.log");
    if (!file.is_open()) {
        std::cerr << "无法打开文件!" << std::endl;
        return 1;
    }

    std::string line;
    std::vector<std::string> logData;
    bool foundX24814903300 = false;

    // 反向读取文件内容
    while (std::getline(file, line)) {
        logData.push_back(line);
        if (line.find("X24814903300") != std::string::npos) {
            foundX24814903300 = true;
            break; // 找到后停止读取
        }
    }

    if (!foundX24814903300) {
        std::cerr << "未找到 X24814903300!" << std::endl;
        return 1;
    }

    RollData result;
    std::size_t index = logData.size() - 1; // 从最后一行开始

    // 解析 MATNO
    while (index < logData.size()) {
        if (logData[index].find("ID") != std::string::npos) {
            // 找到 ID 行，提取 MATNO
            std::regex matNoRegex(R"(MATNO\s+(\d+))");
            std::smatch match;
            if (std::regex_search(logData[index - 1], match, matNoRegex)) {
                result.matNo = match[1];
            }
        }

        // 查找 P 开头的行
        if (starts_with(logData[index], "P")) {
            for (size_t i = 1; i <= 7; ++i) { // 读取接下来的 7 行
                if (index + i < logData.size()) {
                    std::istringstream iss(logData[index + i]);
                    std::string crt, wear;
                    iss >> crt >> wear; // 读取 CRT 和 WEAR
                    result.crtWearData.emplace_back(crt, wear); // 存储 CRT 和 WEAR 数据
                }
            }
            break; // 找到后停止
        }
        --index; // 向上移动
    }

    // 输出结果
    std::cout << "MATNO: " << result.matNo << std::endl;
    std::cout << "CRT 和 WEAR 数据:" << std::endl;
    for (const auto& data : result.crtWearData) {
        std::cout << "CRT: " << data.first << ", WEAR: " << data.second << std::endl;
    }

    return 0;
}