#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

struct RollData {
    std::string type;
    std::string rollNumber;
    std::string diameter;
    std::string quality;
    std::string grindType;
};

int main() {
    // std::ifstream file("e:\\OneDrive\\Desktop\\RollData-240812.log");
    std::ifstream file("RollData-240812.log");
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

    for (size_t i = 0; i < stand7Data.size(); ++i) {
        const std::string& entry = stand7Data[i]; // 使用 const 引用
        // 查找并提取信息
        std::string type, rollNumber, diameter, quality, grindType;
        std::size_t pos = entry.find("Stand 7");
        if (pos != std::string::npos) {
            std::istringstream iss(entry.substr(pos + 8)); // 跳过 "Stand 7 "
            iss >> type >> rollNumber; // 读取类型和卷号
            std::string diaLabel;
            iss >> diaLabel; // 读取 "Dia"
            if (diaLabel == "Dia") {
                iss >> diameter; // 读取直径
                std::string qualLabel;
                iss >> qualLabel; // 读取 "Qual="
                if (qualLabel == "Qual=") {
                    iss >> quality; // 读取质量
                    std::string grindLabel;
                    iss >> grindLabel; // 读取 "Grindtyp="
                    if (grindLabel == "Grindtyp=") {
                        iss >> grindType; // 读取磨削类型
                    }
                }
            }
            // results.push_back({type, rollNumber, diameter, quality, grindType});
            // 使用构造函数创建 RollData 对象并添加到 results
            RollData data;
            data.type = type;
            data.rollNumber = rollNumber;
            data.diameter = diameter;
            data.quality = quality;
            data.grindType = grindType;
            results.push_back(data); // 使用 push_back 添加对象
        }
    }

    // 输出结果
    for (size_t i = 0; i < results.size(); ++i) {
        const RollData& result = results[i]; // 使用 const 引用
        std::cout << "Type: " << result.type 
                  << ", Roll Number: " << result.rollNumber 
                  << ", Diameter: " << result.diameter 
                  << ", Quality: " << result.quality 
                  << ", Grind Type: " << result.grindType << std::endl;
    }

    return 0;
}