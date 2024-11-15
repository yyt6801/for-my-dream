# -*- coding: utf-8 -*-
from flask import Flask, make_response
from flask import Flask, request, send_file
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.backends.backend_pdf import PdfPages
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

app = Flask(__name__)
# 注册支持中文的字体
pdfmetrics.registerFont(TTFont('SimHei', 'SimHei.ttf'))  # SimHei.ttf 是一个支持中文的字体文件，需要提前下载并放置在项目目录中

@app.route('/export_pdf_report', methods=['GET'])
def export_pdf_report():
    # # 创建一个BytesIO对象，用于在内存中临时存储PDF数据
    # packet = io.BytesIO()

    # 1. 使用matplotlib绘制图表（这里简单绘制一个折线图示例）
    sample_data = [0.757, 0.759, 0.755, 0.763, 0.756, 0.755, 0.761, 0.756, 0.757, 0.756, 0.756, 0.753, 0.754, 0.757, 0.743, 0.757, 0.758, 0.757, 0.756, 0.758, 0.759, 0.757, 0.757, 0.758, 0.754, 0.759, 0.756, 0.759, 0.753, 0.757, 0.76, 0.758, 0.757, 0.755, 0.759, 0.758, 0.759, 0.757, 0.757, 0.755, 0.759, 0.751, 0.759, 0.758, 0.757, 0.755, 0.757, 0.755, 0.754, 0.757, 0.757, 0.755, 0.759, 0.758, 0.753, 0.756, 0.758, 0.758, 0.76, 0.754, 0.759, 0.757, 0.756, 0.761, 0.756, 0.759, 0.758, 0.757, 0.758, 0.752, 0.758, 0.757, 0.759, 0.759, 0.757, 0.758, 0.758, 0.759, 0.756, 0.759, 0.757, 0.755, 0.755, 0.755, 0.757, 0.76, 0.759, 0.757, 0.763, 0.753, 0.757, 0.759, 0.758, 0.756, 0.755, 0.757, 0.76, 0.757, 0.746, 0.764, 0.759, 0.759, 0.766, 0.758, 0.755, 0.759, 0.757, 0.757, 0.761, 0.759, 0.755, 0.757, 0.758, 0.757, 0.757, 0.758, 0.759, 0.756, 0.758, 0.758, 0.758, 0.758, 0.758, 0.834, 0.824, 0.759, 0.757, 0.752, 0.755, 0.755, 0.748, 0.762, 0.761, 0.761, 0.756, 0.76, 0.762, 0.758, 0.755, 0.76, 0.763, 0.764, 0.757, 0.76, 0.761, 0.758, 0.76, 0.758, 0.756, 0.762, 0.76, 0.762, 0.758, 0.763, 0.761, 0.762, 0.759, 0.76, 0.759, 0.765, 0.759, 0.761, 0.758, 0.76, 0.761, 0.754, 0.76, 0.762, 0.756, 0.759, 0.755, 0.76, 0.754, 0.758, 0.755, 0.759, 0.758, 0.758, 0.758, 0.758, 0.756, 0.756, 0.758, 0.758, 0.754, 0.757, 0.759, 0.754, 0.757, 0.758, 0.755, 0.76, 0.754, 0.755, 0.755, 0.755, 0.757, 0.754, 0.754, 0.757, 0.756, 0.755, 0.752, 0.757, 0.755, 0.757, 0.756, 0.759, 0.755, 0.754, 0.755, 0.753, 0.752, 0.756, 0.766, 0.747, 0.763, 0.746, 0.762, 0.746, 0.756, 0.756, 0.748, 0.753, 0.761, 0.745, 0.753, 0.754, 0.745, 0.767, 0.76, 0.749, 0.743, 0.763, 0.759, 0.752, 0.74, 0.75, 0.767, 0.748, 0.747, 0.753, 0.754, 0.749, 0.758, 0.745, 0.757, 0.745, 0.792, 0.817, 0.828]
    sample_range =[0.011,0.010,0.016,0.017,0.009,0.019,0.023,0.011,0.018,0.015,0.008,0.018,0.017,0.015,0.027,0.014,0.012,0.015,0.017,0.026,0.022,0.017,0.023,0.011,0.022,0.016,0.018,0.019,0.011,0.023,0.014,0.019,0.024,0.022,0.011,0.016,0.020,0.021,0.019,0.011,0.011,0.020,0.014,0.015,0.015,0.014,0.017,0.023,0.025,0.012,0.012,0.019,0.017,0.015,0.017,0.013,0.022,0.020,0.033,0.014,0.014,0.016,0.011,0.018,0.023,0.015,0.022,0.010,0.021,0.016,0.014,0.019,0.020,0.019,0.023,0.018,0.010,0.017,0.017,0.012,0.013,0.011,0.014,0.021,0.015,0.017,0.018,0.012,0.019,0.024,0.014,0.026,0.015,0.026,0.024,0.020,0.016,0.018,0.031,0.010,0.015,0.012,0.018,0.030,0.016,0.011,0.011,0.014,0.019,0.018,0.023,0.020,0.023,0.007,0.011,0.013,0.019,0.015,0.023,0.013,0.012,0.011,0.017,0.077,0.081,0.010,0.017,0.011,0.019,0.015,0.037,0.008,0.011,0.011,0.019,0.018,0.026,0.012,0.014,0.022,0.032,0.034,0.012,0.018,0.013,0.024,0.018,0.015,0.013,0.016,0.010,0.014,0.010,0.027,0.008,0.015,0.017,0.013,0.025,0.022,0.029,0.018,0.016,0.026,0.013,0.023,0.010,0.021,0.020,0.019,0.015,0.012,0.025,0.012,0.021,0.018,0.014,0.007,0.025,0.018,0.028,0.014,0.011,0.013,0.019,0.013,0.014,0.023,0.012,0.015,0.021,0.021,0.017,0.010,0.022,0.015,0.015,0.026,0.017,0.010,0.015,0.014,0.021,0.015,0.013,0.029,0.015,0.014,0.017,0.019,0.025,0.014,0.025,0.023,0.083,0.013,0.019,0.015,0.013,0.017,0.009,0.019,0.011,0.013,0.023,0.012,0.011,0.017,0.015,0.049,0.021,0.016,0.018,0.026,0.021,0.025,0.021,0.016,0.024,0.018,0.006,0.014,0.014,0.012,0.016,0.011,0.032,0.011,0.052,0.091,0.231]
    sample_stdev=[0.00,0.00,0.01,0.00,0.00,0.00,0.01,0.00,0.01,0.00,0.00,0.01,0.01,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.01,0.01,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.00,0.01,0.01,0.01,0.00,0.01,0.01,0.01,0.01,0.00,0.00,0.01,0.00,0.00,0.00,0.00,0.00,0.01,0.01,0.00,0.00,0.01,0.00,0.00,0.01,0.00,0.01,0.01,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.01,0.01,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.00,0.01,0.00,0.01,0.01,0.01,0.00,0.00,0.01,0.00,0.00,0.00,0.01,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.01,0.01,0.01,0.00,0.00,0.00,0.01,0.00,0.01,0.00,0.00,0.00,0.00,0.03,0.03,0.00,0.00,0.00,0.01,0.01,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.00,0.00,0.01,0.01,0.01,0.00,0.01,0.00,0.01,0.01,0.00,0.00,0.00,0.00,0.00,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.01,0.00,0.00,0.01,0.00,0.01,0.00,0.01,0.01,0.01,0.00,0.00,0.01,0.00,0.01,0.01,0.00,0.00,0.01,0.00,0.01,0.00,0.00,0.00,0.01,0.00,0.00,0.01,0.00,0.00,0.01,0.00,0.01,0.00,0.01,0.01,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.00,0.00,0.01,0.00,0.00,0.00,0.01,0.01,0.00,0.01,0.01,0.03,0.00,0.01,0.00,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.00,0.00,0.00,0.00,0.02,0.01,0.01,0.00,0.01,0.01,0.01,0.01,0.00,0.01,0.01,0.00,0.00,0.00,0.00,0.00,0.00,0.01,0.00,0.02,0.03,0.05]
    
    # ****************************************************************************************
    data = np.array(sample_data)  # 替换为你的实际数据
    max_=np.max(data)
    min_=np.min(data)

    # 规格限
    USL = 0.89  # 上规格限
    LSL = 0.55  # 下规格限

    # 计算均值和标准差
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  # 使用样本标准差

    # 计算Cp和Cpk
    Cp = (USL - LSL) / (6 * std_dev)
    Cpk = min((USL - mean) / (3 * std_dev), (mean - LSL) / (3 * std_dev))
    Cpk1 = min((max_ - mean) / (3 * std_dev), (mean - min_) / (3 * std_dev))
    Cpk2 = (max_-min_)/(6*std_dev) * (1-(mean-(max_+min_)/2)/(max_-min_)/2)

    # 计算Pp和Ppk
    Pp = (USL - LSL) / (6 * np.std(data, ddof=0))  # 使用总体标准差
    Ppk = min((USL - mean) / (3 * np.std(data, ddof=0)), (mean - LSL) / (3 * np.std(data, ddof=0)))

    print(f"Mean: {mean:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
    print(f"Cp: {Cp:.2f}")
    print(f"Cpk: {Cpk:.2f}")
    print(f"Cpk1: {Cpk1:.2f}")
    print(f"Cpk2: {Cpk2:.2f}")
    print(f"Pp: {Pp:.2f}")
    print(f"Ppk: {Ppk:.2f}")
        
    means = data
    ranges = sample_range
    std_devs = sample_stdev

    # 计算总体均值、平均极差和平均标准差
    overall_mean = np.mean(means)
    average_range = np.mean(ranges)
    average_std_dev = np.mean(std_devs)

    # 控制图常数（假设样本大小为4）
    A2 = 0.729
    D3 = 0
    D4 = 2.282
    B3 = 0
    B4 = 2.266

    # 计算控制限
    UCL_X = overall_mean + A2 * average_range
    LCL_X = overall_mean - A2 * average_range
    UCL_R = D4 * average_range
    LCL_R = D3 * average_range
    UCL_S = B4 * average_std_dev
    LCL_S = B3 * average_std_dev
    
    # # 创建PDF文件
    # pdf_filename = "SPC_Charts.pdf"
    # pdf = PdfPages(pdf_filename)
    
    # 创建PDF文件
    pdf_buffer = io.BytesIO()
    pdf = PdfPages(pdf_buffer)

    # 绘制X-bar控制图
    plt.figure(figsize=(8, 4))
    plt.plot(means, marker='o', linestyle='-')
    plt.axhline(overall_mean, color='green', linestyle='--', label='CL')
    plt.axhline(UCL_X, color='red', linestyle='--', label='UCL')
    plt.axhline(LCL_X, color='red', linestyle='--', label='LCL')
    plt.title('X-bar Control Chart')
    plt.xlabel('Sample Group')
    plt.ylabel('Mean')
    plt.legend()
    plt.text(0.5, 0.01, 'X-bar chart shows the mean of each sample group.', ha='center', va='center', transform=plt.gcf().transFigure)
    pdf.savefig()  # 保存当前图表到PDF
    plt.close()

    # 绘制R控制图
    plt.figure(figsize=(8, 4))
    plt.plot(ranges, marker='o', linestyle='-')
    plt.axhline(average_range, color='green', linestyle='--', label='CL')
    plt.axhline(UCL_R, color='red', linestyle='--', label='UCL')
    plt.axhline(LCL_R, color='red', linestyle='--', label='LCL')
    plt.title('R Control Chart')
    plt.xlabel('Sample Group')
    plt.ylabel('Range')
    plt.legend()
    plt.text(0.5, 0.01, 'R chart shows the range of each sample group.', ha='center', va='center', transform=plt.gcf().transFigure)
    pdf.savefig()
    plt.close()

    # 绘制S控制图
    plt.figure(figsize=(8, 4))
    plt.plot(std_devs, marker='o', linestyle='-')
    plt.axhline(average_std_dev, color='green', linestyle='--', label='CL')
    plt.axhline(UCL_S, color='red', linestyle='--', label='UCL')
    plt.axhline(LCL_S, color='red', linestyle='--', label='LCL')
    plt.title('S Control Chart')
    plt.xlabel('Sample Group')
    plt.ylabel('Standard Deviation')
    plt.legend()
    plt.text(0.5, 0.01, 'S chart shows the standard deviation of each sample group.', ha='center', va='center', transform=plt.gcf().transFigure)
    pdf.savefig()
    plt.close()

    # 绘制QQ图
    plt.figure(figsize=(8, 6))
    stats.probplot(data.flatten(), dist="norm", plot=plt)
    plt.title('QQ Plot')
    pdf.savefig()
    plt.close()

    # 绘制分布直方图和正态分布曲线
    plt.figure(figsize=(8, 4))
    n, bins, patches = plt.hist(data.flatten(), bins=10, color='skyblue', edgecolor='black', alpha=0.7, density=True)

    # 计算正态分布曲线
    mu, sigma = np.mean(data.flatten()), np.std(data.flatten(), ddof=1)
    x = np.linspace(min(data.flatten()), max(data.flatten()), 100)
    y = stats.norm.pdf(x, mu, sigma)
    plt.plot(x, y, color='darkblue', linewidth=2, label='Normal Distribution')

    # 添加控制目标和6西格玛线
    target = overall_mean
    plt.axvline(target, color='purple', linestyle='--', linewidth=2, label='Target')
    plt.axvline(target + 3 * sigma, color='orange', linestyle='--', linewidth=2, label='+3σ')
    plt.axvline(target - 3 * sigma, color='orange', linestyle='--', linewidth=2, label='-3σ')
    plt.axvline(target + 6 * sigma, color='red', linestyle='--', linewidth=2, label='+6σ')
    plt.axvline(target - 6 * sigma, color='red', linestyle='--', linewidth=2, label='-6σ')

    plt.title('Histogram and Normal Distribution Curve')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    plt.legend()
    plt.text(0.5, 0.01, 'Histogram with normal distribution curve.', ha='center', va='center', transform=plt.gcf().transFigure)
    # plt.grid(axis='y', alpha=0.75)
    pdf.savefig()
    plt.close()

    # 关闭PDF文件
    pdf.close()
    pdf_buffer.seek(0)

    return send_file(pdf_buffer, as_attachment=True, download_name='SPC_Report.pdf', mimetype='application/pdf')

    # # 使用reportlab添加封面
    # c = canvas.Canvas("SPC_Charts_with_Cover.pdf", pagesize=letter)
    # c.setFont("Helvetica", 20)
    # c.drawString(100, 750, "SPC Analysis Report")
    # c.setFont("Helvetica", 12)
    # c.drawString(100, 730, "This report contains SPC charts and analysis results.")
    # c.showPage()
    # c.save()

    # # 将生成的图表PDF合并到封面PDF中
    # from PyPDF2 import PdfReader, PdfWriter

    # cover_pdf = PdfReader("SPC_Charts_with_Cover.pdf")
    # charts_pdf = PdfReader(pdf_filename)
    # output_pdf = PdfWriter()

    # # 添加封面
    # output_pdf.add_page(cover_pdf.pages[0])

    # # 添加图表
    # for page in charts_pdf.pages:
    #     output_pdf.add_page(page)

    # # 保存最终PDF
    # with open("Final_SPC_Report.pdf", "wb") as f:
    #     output_pdf.write(f)

    # print("PDF report generated: Final_SPC_Report.pdf")
    # # 6. 将内存中的PDF数据获取出来，作为响应返回给客户端
    # packet.seek(0)
    # response = make_response(packet.read())
    # response.headers['Content-Type'] = 'application/pdf'
    # response.headers['Content-Disposition'] = 'attachment; filename=report.pdf'
    # return response

if __name__ == '__main__':
    app.run(debug=True)