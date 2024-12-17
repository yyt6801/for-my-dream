# -*- coding: utf-8 -*-
from flask import Flask, request, send_file
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime, timedelta
import http.client
import json

def replace_last_word(s, replacement):  
    # 从右侧分割字符串，最多分割成2部分  
    parts = s.rsplit('_', 1)  
    if len(parts) == 2:  
        # 用替换的单词组合字符串  
        return f"{parts[0]}_{replacement}"  
    else:  
        # 如果没有下划线，直接返回原字符串  
        return s  

def query_data(sample_avg_name, sample_range_name, sample_stdev_name,begin_time, end_time, steel_grade, thick_targ, limit_low, limit_high):
    conn = http.client.HTTPConnection("10.151.18.218", 8086)
    payload = json.dumps({
        "sql": "select "+sample_avg_name +","+sample_range_name +","+sample_stdev_name+" from V_TCM_CONTROL_SPC_PART2 t @where",
        "@where": "where PROD_END_TIME > to_char(to_date('"+begin_time+"','yyyy-mm-dd hh24:mi:ss'),'yyyymmddhh24miss') and PROD_END_TIME < to_char(to_date('"+end_time+"','yyyy-mm-dd hh24:mi:ss'),'yyyymmddhh24miss') and STEEL_GRADE = '"+steel_grade+"' and t.thick_targ between "+str(limit_low)+" and "+str(limit_high)+" and t.thick_targ = "+str(thick_targ)+" and "+sample_avg_name +" > 0",
        "db": "ORAINS"
    })
    # 'Host': '10.151.18.218:8086',
    headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Connection': 'keep-alive'
    }
    conn.request("POST", "/DB_Query", payload, headers)
    print(payload)
    res = conn.getresponse()
    data = res.read()
    return data

def get_request_params():
    # 获取GET请求的参数
    sample_avg_name = request.args.get('sample_avg_name', 'S5_THK_HEAD_AVG')
    sample_range_name = replace_last_word(sample_avg_name, 'RANGE')
    sample_stdev_name = replace_last_word(sample_avg_name, 'STDDEV')
    parameter = request.args.get('parameter', '5机架厚度头部均值')
    BEGINTIME = request.args.get('begintime', (datetime.now()-timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S'))
    ENDTIME = request.args.get('endtime', (datetime.now()).strftime('%Y-%m-%d %H:%M:%S'))
    STEELGRADE = request.args.get('steelgrade', "SPHC-Z")
    USL = request.args.get('usl', 0.89)
    LSL = request.args.get('lsl', 0.55)
    TARGET = request.args.get('target', 0.77)
    
    # 解析字符串
    try:
        sample_avg_name = json.loads(sample_avg_name)
    except json.JSONDecodeError:
        pass

    try:
        sample_range_name = json.loads(sample_range_name)
    except json.JSONDecodeError:
        pass

    try:
        sample_stdev_name = json.loads(sample_stdev_name)
    except json.JSONDecodeError:
        pass

    try:
        BEGINTIME = json.loads(BEGINTIME)
    except json.JSONDecodeError:
        pass

    try:
        ENDTIME = json.loads(ENDTIME)
    except json.JSONDecodeError:
        pass

    return sample_avg_name, sample_range_name, sample_stdev_name, BEGINTIME, ENDTIME, STEELGRADE, TARGET, USL, LSL, parameter

def get_post_request_params():
    # 获取POST请求的参数
    sample_avg_name = request.form.get('sample_avg_name', 'S5_THK_HEAD_AVG')
    sample_range_name = replace_last_word(sample_avg_name, 'RANGE')
    sample_stdev_name = replace_last_word(sample_avg_name, 'STDDEV')
    parameter = request.form.get('parameter', '5机架厚度头部均值')
    BEGINTIME = request.form.get('begintime', (datetime.now()-timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S'))
    ENDTIME = request.form.get('endtime', (datetime.now()).strftime('%Y-%m-%d %H:%M:%S'))
    STEELGRADE = request.form.get('steelgrade', "SPHC-Z")
    USL = request.form.get('uplimit', 0.89)
    LSL = request.form.get('lowlimit', 0.55)
    TARGET = request.form.get('objectives', 0.77)
    
    # 解析字符串
    try:
        sample_avg_name = json.loads(sample_avg_name)
    except json.JSONDecodeError:
        pass

    try:
        sample_range_name = json.loads(sample_range_name)
    except json.JSONDecodeError:
        pass

    try:
        sample_stdev_name = json.loads(sample_stdev_name)
    except json.JSONDecodeError:
        pass

    try:
        BEGINTIME = json.loads(BEGINTIME)
    except json.JSONDecodeError:
        pass

    try:
        ENDTIME = json.loads(ENDTIME)
    except json.JSONDecodeError:
        pass

    return sample_avg_name, sample_range_name, sample_stdev_name, BEGINTIME, ENDTIME, STEELGRADE, TARGET, USL, LSL, parameter

app = Flask(__name__)
pdfmetrics.registerFont(TTFont('SimHei', 'SimHei.ttf'))

@app.route('/export_pdf_report', methods=['POST'])
def export_pdf_report_post():
    sample_avg_name, sample_range_name, sample_stdev_name, BEGINTIME, ENDTIME, STEELGRADE, TARGET, USL, LSL, parameter = get_post_request_params()
    return generate_pdf_report(sample_avg_name, sample_range_name, sample_stdev_name, BEGINTIME, ENDTIME, STEELGRADE, TARGET, USL, LSL, parameter)

@app.route('/export_pdf_report', methods=['GET'])
def export_pdf_report_get():
    sample_avg_name, sample_range_name, sample_stdev_name, BEGINTIME, ENDTIME, STEELGRADE, TARGET, USL, LSL, parameter = get_request_params()
    return generate_pdf_report(sample_avg_name, sample_range_name, sample_stdev_name, BEGINTIME, ENDTIME, STEELGRADE, TARGET, USL, LSL, parameter)

def generate_pdf_report(sample_avg_name, sample_range_name, sample_stdev_name, BEGINTIME, ENDTIME, STEELGRADE, TARGET, USL, LSL, parameter):
    response = query_data(sample_avg_name, sample_range_name, sample_stdev_name, BEGINTIME, ENDTIME, STEELGRADE, TARGET, LSL, USL)
    sample_data = []
    sample_range =[]
    sample_stdev =[]
    data = json.loads(response)
    if 'data' in data:
        res = data["data"]
        for i in range(len(res)):
            sample_data.append(res[i][sample_avg_name])
            sample_range.append(res[i][sample_range_name])
            sample_stdev.append(res[i][sample_stdev_name])
        # 1. 使用matplotlib绘制图表（这里简单绘制一个折线图示例）
        #sample_data = [0.757, 0.759, 0.755, 0.763, 0.756, 0.755, 0.761, 0.756, 0.757, 0.756, 0.756, 0.753, 0.754, 0.757, 0.743, 0.757, 0.758, 0.757, 0.756, 0.758, 0.759, 0.757, 0.757, 0.758, 0.754, 0.759, 0.756, 0.759, 0.753, 0.757, 0.76, 0.758, 0.757, 0.755, 0.759, 0.758, 0.759, 0.757, 0.757, 0.755, 0.759, 0.751, 0.759, 0.758, 0.757, 0.755, 0.757, 0.755, 0.754, 0.757, 0.757, 0.755, 0.759, 0.758, 0.753, 0.756, 0.758, 0.758, 0.76, 0.754, 0.759, 0.757, 0.756, 0.761, 0.756, 0.759, 0.758, 0.757, 0.758, 0.752, 0.758, 0.757, 0.759, 0.759, 0.757, 0.758, 0.758, 0.759, 0.756, 0.759, 0.757, 0.755, 0.755, 0.755, 0.757, 0.76, 0.759, 0.757, 0.763, 0.753, 0.757, 0.759, 0.758, 0.756, 0.755, 0.757, 0.76, 0.757, 0.746, 0.764, 0.759, 0.759, 0.766, 0.758, 0.755, 0.759, 0.757, 0.757, 0.761, 0.759, 0.755, 0.757, 0.758, 0.757, 0.757, 0.758, 0.759, 0.756, 0.758, 0.758, 0.758, 0.758, 0.758, 0.834, 0.824, 0.759, 0.757, 0.752, 0.755, 0.755, 0.748, 0.762, 0.761, 0.761, 0.756, 0.76, 0.762, 0.758, 0.755, 0.76, 0.763, 0.764, 0.757, 0.76, 0.761, 0.758, 0.76, 0.758, 0.756, 0.762, 0.76, 0.762, 0.758, 0.763, 0.761, 0.762, 0.759, 0.76, 0.759, 0.765, 0.759, 0.761, 0.758, 0.76, 0.761, 0.754, 0.76, 0.762, 0.756, 0.759, 0.755, 0.76, 0.754, 0.758, 0.755, 0.759, 0.758, 0.758, 0.758, 0.758, 0.756, 0.756, 0.758, 0.758, 0.754, 0.757, 0.759, 0.754, 0.757, 0.758, 0.755, 0.76, 0.754, 0.755, 0.755, 0.755, 0.757, 0.754, 0.754, 0.757, 0.756, 0.755, 0.752, 0.757, 0.755, 0.757, 0.756, 0.759, 0.755, 0.754, 0.755, 0.753, 0.752, 0.756, 0.766, 0.747, 0.763, 0.746, 0.762, 0.746, 0.756, 0.756, 0.748, 0.753, 0.761, 0.745, 0.753, 0.754, 0.745, 0.767, 0.76, 0.749, 0.743, 0.763, 0.759, 0.752, 0.74, 0.75, 0.767, 0.748, 0.747, 0.753, 0.754, 0.749, 0.758, 0.745, 0.757, 0.745, 0.792, 0.817, 0.828]
        #sample_range =[0.011,0.010,0.016,0.017,0.009,0.019,0.023,0.011,0.018,0.015,0.008,0.018,0.017,0.015,0.027,0.014,0.012,0.015,0.017,0.026,0.022,0.017,0.023,0.011,0.022,0.016,0.018,0.019,0.011,0.023,0.014,0.019,0.024,0.022,0.011,0.016,0.020,0.021,0.019,0.011,0.011,0.020,0.014,0.015,0.015,0.014,0.017,0.023,0.025,0.012,0.012,0.019,0.017,0.015,0.017,0.013,0.022,0.020,0.033,0.014,0.014,0.016,0.011,0.018,0.023,0.015,0.022,0.010,0.021,0.016,0.014,0.019,0.020,0.019,0.023,0.018,0.010,0.017,0.017,0.012,0.013,0.011,0.014,0.021,0.015,0.017,0.018,0.012,0.019,0.024,0.014,0.026,0.015,0.026,0.024,0.020,0.016,0.018,0.031,0.010,0.015,0.012,0.018,0.030,0.016,0.011,0.011,0.014,0.019,0.018,0.023,0.020,0.023,0.007,0.011,0.013,0.019,0.015,0.023,0.013,0.012,0.011,0.017,0.077,0.081,0.010,0.017,0.011,0.019,0.015,0.037,0.008,0.011,0.011,0.019,0.018,0.026,0.012,0.014,0.022,0.032,0.034,0.012,0.018,0.013,0.024,0.018,0.015,0.013,0.016,0.010,0.014,0.010,0.027,0.008,0.015,0.017,0.013,0.025,0.022,0.029,0.018,0.016,0.026,0.013,0.023,0.010,0.021,0.020,0.019,0.015,0.012,0.025,0.012,0.021,0.018,0.014,0.007,0.025,0.018,0.028,0.014,0.011,0.013,0.019,0.013,0.014,0.023,0.012,0.015,0.021,0.021,0.017,0.010,0.022,0.015,0.015,0.026,0.017,0.010,0.015,0.014,0.021,0.015,0.013,0.029,0.015,0.014,0.017,0.019,0.025,0.014,0.025,0.023,0.083,0.013,0.019,0.015,0.013,0.017,0.009,0.019,0.011,0.013,0.023,0.012,0.011,0.017,0.015,0.049,0.021,0.016,0.018,0.026,0.021,0.025,0.021,0.016,0.024,0.018,0.006,0.014,0.014,0.012,0.016,0.011,0.032,0.011,0.052,0.091,0.231]
        #sample_stdev=[0.00,0.00,0.01,0.00,0.00,0.00,0.01,0.00,0.01,0.00,0.00,0.01,0.01,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.01,0.01,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.00,0.01,0.01,0.01,0.00,0.01,0.01,0.01,0.01,0.00,0.00,0.01,0.00,0.00,0.00,0.00,0.00,0.01,0.01,0.00,0.00,0.01,0.00,0.00,0.01,0.00,0.01,0.01,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.01,0.01,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.00,0.01,0.00,0.01,0.01,0.01,0.00,0.00,0.01,0.00,0.00,0.00,0.01,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.01,0.01,0.01,0.00,0.00,0.00,0.01,0.00,0.01,0.00,0.00,0.00,0.00,0.03,0.03,0.00,0.00,0.00,0.01,0.01,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.00,0.00,0.01,0.01,0.01,0.00,0.01,0.00,0.01,0.01,0.00,0.00,0.00,0.00,0.00,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.01,0.01,0.00,0.00,0.01,0.00,0.01,0.00,0.01,0.01,0.01,0.00,0.00,0.01,0.00,0.01,0.01,0.00,0.00,0.01,0.00,0.01,0.00,0.00,0.00,0.01,0.00,0.00,0.01,0.00,0.00,0.01,0.00,0.01,0.00,0.01,0.01,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.00,0.00,0.01,0.00,0.00,0.00,0.01,0.01,0.00,0.01,0.01,0.03,0.00,0.01,0.00,0.00,0.01,0.00,0.00,0.00,0.00,0.01,0.00,0.00,0.00,0.00,0.02,0.01,0.01,0.00,0.01,0.01,0.01,0.01,0.00,0.01,0.01,0.00,0.00,0.00,0.00,0.00,0.00,0.01,0.00,0.02,0.03,0.05]
        
        # Constants
        A2 = 0.729
        D3 = 0
        D4 = 2.282
        B3 = 0
        B4 = 2.266

        # Data calculations
        data = np.array(sample_data)
        means = data
        ranges = sample_range
        std_devs = sample_stdev
        max_ = np.max(data)
        min_ = np.min(data)
        mean = np.mean(data)
        std_dev = np.std(data, ddof=1)
        overall_mean = np.mean(means)
        average_range = np.mean(ranges)
        average_std_dev = np.mean(std_devs)
        total_count = len(data)

        # Capability calculations
        Cp = (USL - LSL) / (6 * std_dev)
        Cpk = min((USL - mean) / (3 * std_dev), (mean - LSL) / (3 * std_dev))
        Pp = (USL - LSL) / (6 * np.std(data, ddof=0))
        Ppk = min((USL - mean) / (3 * np.std(data, ddof=0)), (mean - LSL) / (3 * np.std(data, ddof=0)))

        # Control limits
        UCL_X = overall_mean + A2 * average_range
        LCL_X = overall_mean - A2 * average_range
        UCL_R = D4 * average_range
        LCL_R = D3 * average_range
        UCL_S = B4 * average_std_dev
        LCL_S = B3 * average_std_dev

        # PDF generation
        report_buffer = io.BytesIO()
        doc = SimpleDocTemplate(report_buffer, pagesize=letter)
        elements = []

        # Styles
        style_normal = ParagraphStyle(name='Normal', fontName='SimHei', fontSize=12, leading=14)
        title = Paragraph("TCM2 "+str(STEELGRADE)+ " "+str(parameter), ParagraphStyle(name='Title', fontName='SimHei', fontSize=24, leading=14, textColor=colors.black, alignment=1, spaceAfter=12))
        elements.append(title)
        elements.append(Spacer(1, 12))  
        title = Paragraph("SPC过程能力分析报告", ParagraphStyle(name='Title', fontName='SimHei', fontSize=24, textColor=colors.black, alignment=1, spaceAfter=12))
        elements.append(title)
        elements.append(Spacer(1, 12))  
        # 添加一段文字  
        text = Paragraph("--Report Time: " + str(datetime.now()), ParagraphStyle(name='Normal', fontSize=10, alignment=2))  
        elements.append(text)  
        elements.append(Spacer(1, 12))  


        # Helper function for table creation
        def create_table(data, col_widths):
            table = Table(data, colWidths=col_widths)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, -1), 'SimHei'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            return table

        # Add tables
        data_left = [
            ['--', '样本信息'],
            ['开始时间', str(BEGINTIME)],
            ['结束时间', str(ENDTIME)],
            ['钢种', str(STEELGRADE)],
            ['控制上限', f'{USL:.3f}'],
            ['控制下限', f'{LSL:.3f}'],
            ['目标值', f'{TARGET:.3f}'],
            ['样本总数', f'{total_count}'],
        ]
        data_table = [
            ['过程能力指标', '能力值'],
            ['Overall Mean', f'{overall_mean:.3f}'],
            ['Average Range', f'{average_range:.3f}'],
            ['Average Std Dev', f'{average_std_dev:.3f}'],
            ['Cp', f'{Cp:.3f}'],
            ['Cpk', f'{Cpk:.3f}'],
            ['Pp', f'{Pp:.3f}'],
            ['Ppk', f'{Ppk:.3f}'],
        ]
        combined_table = Table([[create_table(data_left, [110]), create_table(data_table, [110])]], colWidths=[250, 250])
        elements.append(combined_table)
        elements.append(Spacer(1, 12))

        # Plotting functions
        def save_plot_to_buffer(fig):
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)
            return buf

        # X-bar chart
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(means, marker='o', linestyle='-')
        ax.axhline(overall_mean, color='green', linestyle='--', label='CL')
        ax.axhline(UCL_X, color='red', linestyle='--', label='UCL')
        ax.axhline(LCL_X, color='red', linestyle='--', label='LCL')
        ax.set_title('X-bar Control Chart')
        ax.set_xlabel('Sample Number')
        ax.set_ylabel('Mean Value')
        ax.legend()
        # Annotate the control limits and center line
        ax.text(len(means) + 15, UCL_X, f'UCL: {UCL_X:.3f}', color='red', va='center', ha='left')
        ax.text(len(means) + 15, LCL_X, f'LCL: {LCL_X:.3f}', color='red', va='center', ha='left')
        ax.text(len(means) + 15, overall_mean, f'CL: {overall_mean:.3f}', color='green', va='center', ha='left')

        img = Image(save_plot_to_buffer(fig),width=600, height=240)  # 请确保图片文件存在  
        img.hAlign = 'CENTER'  # 图片水平居中  
        elements.append(img)
        plt.close(fig)
        paragraph = Paragraph("X-bar控制图: 用于监控样本均值的变化。UCL（上控制限）和LCL（下控制限）用于判断过程是否失控", style_normal)
        elements.append(paragraph)
        elements.append(Spacer(1, 12))

        # R chart
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(ranges, marker='o', linestyle='-')
        ax.axhline(average_range, color='green', linestyle='--', label='CL')
        ax.axhline(UCL_R, color='red', linestyle='--', label='UCL')
        ax.axhline(LCL_R, color='red', linestyle='--', label='LCL')
        ax.set_title('R Control Chart')
        ax.set_xlabel('Sample Number')
        ax.set_ylabel('Range')
        ax.legend()
        # Annotate the control limits and center line
        ax.text(len(means) + 15, UCL_R, f'UCL: {UCL_R:.3f}', color='red', va='center', ha='left')
        ax.text(len(means) + 15, LCL_R, f'LCL: {LCL_R:.3f}', color='red', va='center', ha='left')
        ax.text(len(means) + 15, average_range, f'CL: {average_range:.3f}', color='green', va='center', ha='left')
        img = Image(save_plot_to_buffer(fig),width=600, height=240)  # 请确保图片文件存在  
        img.hAlign = 'CENTER'  # 图片水平居中  
        elements.append(img)
        plt.close(fig)
        paragraph = Paragraph("R控制图: 用于监控样本极差的变化，帮助识别过程的变异性。", style_normal)
        elements.append(paragraph)
        elements.append(Spacer(1, 12))

        # S chart
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(std_devs, marker='o', linestyle='-')
        ax.axhline(average_std_dev, color='green', linestyle='--', label='CL')
        ax.axhline(UCL_S, color='red', linestyle='--', label='UCL')
        ax.axhline(LCL_S, color='red', linestyle='--', label='LCL')
        ax.set_title('S Control Chart')
        ax.set_xlabel('Sample Number')
        ax.set_ylabel('Standard Deviation')
        ax.legend()
        # Annotate the control limits and center line
        ax.text(len(means) + 15, UCL_S, f'UCL: {UCL_S:.3f}', color='red', va='center', ha='left')
        ax.text(len(means) + 15, LCL_S, f'LCL: {LCL_S:.3f}', color='red', va='center', ha='left')
        ax.text(len(means) + 15, average_std_dev, f'CL: {average_std_dev:.3f}', color='green', va='center', ha='left')
        img = Image(save_plot_to_buffer(fig),width=600, height=240)  # 请确保图片文件存在  
        img.hAlign = 'CENTER'  # 图片水平居中  
        elements.append(img)
        plt.close(fig)
        paragraph = Paragraph("S控制图（标准差控制图）: 监控样本标准差的变化。使用标准差来评估过程变异性。", style_normal)
        elements.append(paragraph)
        elements.append(Spacer(1, 12))

        # Histogram and normal distribution curve
        fig, ax = plt.subplots(figsize=(10, 8))
        n, bins, patches = ax.hist(means, bins=10, color='skyblue', edgecolor='black', alpha=0.7, density=True)
        mu, sigma = np.mean(means), np.std(means, ddof=1)
        x = np.linspace(min(means), max(means), 100)
        y = stats.norm.pdf(x, mu, sigma)
        ax.plot(x, y, color='darkblue', linewidth=2, label='Normal Distribution')
        ax.axvline(overall_mean, color='purple', linestyle='--', linewidth=2, label='Target')
        ax.axvline(overall_mean + 3 * sigma, color='orange', linestyle='--', linewidth=2, label='+3σ')
        ax.axvline(overall_mean - 3 * sigma, color='orange', linestyle='--', linewidth=2, label='-3σ')
        ax.axvline(overall_mean + 6 * sigma, color='red', linestyle='--', linewidth=2, label='+6σ')
        ax.axvline(overall_mean - 6 * sigma, color='red', linestyle='--', linewidth=2, label='-6σ')
        ax.set_title('Histogram and Normal Distribution Curve')
        ax.set_xlabel('Value')
        ax.set_ylabel('Density')
        ax.legend()
        img = Image(save_plot_to_buffer(fig),width=600, height=400)  # 请确保图片文件存在  
        img.hAlign = 'CENTER'  # 图片水平居中  
        elements.append(img)
        plt.close(fig)
        paragraph = Paragraph("直方图可以直观地了解数据分布，添加目标和3σ线，可知数据分布相对于目标和控制限的位置，帮助识别潜在的过程偏差和变异。", style_normal)
        elements.append(paragraph)
        paragraph = Paragraph("控制目标（Target）: 在直方图中用紫色虚线表示，通常是过程的目标值或期望值。", style_normal)
        elements.append(paragraph)
        paragraph = Paragraph("3西格玛（3σ）线: 在直方图中用橙色虚线表示，显示在目标值的±3σ位置，帮助识别数据的分布范围。", style_normal)
        elements.append(paragraph)
        elements.append(Spacer(1, 12))

        # Build PDF
        doc.build(elements)
        report_buffer.seek(0)
        return send_file(report_buffer, as_attachment=True, download_name='SPC_Report.pdf', mimetype='application/pdf')
    return 'no data'

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0',port=5000)