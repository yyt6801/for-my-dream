#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <utility> // 添加此行以支持 std::pair

int main() {
    std::ifstream file("prom.smf");
    std::string line;
    bool foundLinestyle = false;
    std::vector<std::pair<double, double>> coordinates;

    while (std::getline(file, line)) {
        // 检查是否找到目标 Linestyle
        if (line.find("Linestyle(1,0,\"meas temp\")") != std::string::npos) {
            foundLinestyle = true;
            continue; // 跳过这一行
        }

        // 如果找到 Linestyle，检查下一行是否是 Line()
        if (foundLinestyle) {
            if (line.find("Line(") != std::string::npos) {
                // 读取 Line() 中的坐标
                while (std::getline(file, line) && line.find(")") == std::string::npos) {
                    std::istringstream iss(line);
                    double x, y;
                    if (iss >> x >> y) {
                        // 使用 std::pair 的构造函数
                        std::pair<double, double> coord(x, y);
                        coordinates.push_back(coord); // 使用 push_back 添加坐标
                    }
                }
                break; // 读取完 Line() 后退出
            }
        }
    }

    // 输出结果
    for (size_t i = 0; i < coordinates.size(); ++i) {
        std::cout << "X: " << coordinates[i].first << ", Y: " << coordinates[i].second << std::endl;
    }

    return 0;
}