#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <regex>

struct RollData {
    std::string type;
    std::string rollNumber;
    std::string diameter;
    std::string quality;
    std::string grindType;
};

int main() {
    std::ifstream file("e:\\OneDrive\\Desktop\\RollData-240812.log");
    if (!file.is_open()) {
        std::cerr << "无法打开文件!" << std::endl;
        return 1;
    }

    std::vector<std::string> stand7Data;
    std::string line;

    // 反向读取文件内容
    while (std::getline(file, line)) {
        // 检查是否包含 "Stand 7"
        if (line.find("Stand 7") != std::string::npos) {
            stand7Data.push_back(line);
            if (stand7Data.size() == 4) { // 只需要最后的四项
                break;
            }
        }
    }

    // 解析所需信息
    std::vector<RollData> results;
    std::regex pattern(R"(Stand 7\s+(WrTop|WrBot|BurTop|BurBot)\s+(\S+)\s+Dia\s+([\d.]+),\s+Qual=\s+(\S+),\s+Grindtyp=\s+(\S+))");
    
    for (const auto& entry : stand7Data) {
        std::smatch match;
        if (std::regex_search(entry, match, pattern)) {
            results.push_back({
                match[1], // Type
                match[2], // Roll Number
                match[3], // Diameter
                match[4], // Quality
                match[5]  // Grind Type
            });
        }
    }

    // 输出结果
    for (const auto& result : results) {
        std::cout << "Type: " << result.type 
                  << ", Roll Number: " << result.rollNumber 
                  << ", Diameter: " << result.diameter 
                  << ", Quality: " << result.quality 
                  << ", Grind Type: " << result.grindType << std::endl;
    }

    return 0;
}