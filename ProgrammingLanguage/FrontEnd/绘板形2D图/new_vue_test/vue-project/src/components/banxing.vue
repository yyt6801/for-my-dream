<template>
  <div class="greetings">
    <div id="banxing">
      <h1 class="green"></h1>
      <input id="mat_no" placeholder="卷号" v-model="mat_no" />
      <input type="button" value="查询" @click="draw_echarts()" />
      <br>
      <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
      <div id="main" style="width: 1000px; height: 250px"></div>
      <div id="flatnessmap_2d" style="width: 1000px; height: 350px"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Echarts from "echarts";
export default {
  data() {
    return {
      mat_no: "C231050020",
    };
  },
  methods: {
    draw_echarts() {
      var mat_no = this.mat_no;
      var data = {}
      this.MDB_Query(mat_no, data)
      this.MDB_Query_flatness(mat_no, data)

    },
    async MDB_Query(req_matid, data) {
      const _this = this
      data = await axios.post('/api/MDB_Query',
        JSON.stringify(
          {
            "coll_name": "pltcm_asc_result",
            "filter": {
              "extid": req_matid
            }
          })
      ).then(res => {
        console.log(res.data);
        var data1 = [];
        data1 = res.data.data[0].priterm
        let X = [];
        let coil_length = data1.length
        // for (var i = 0; i < coil_length; i++) {
        //   X.push(i)
        // }
        for (var i = coil_length; i >0; i--) {
          X.push(i)
        }
        var datax = X;
        _this.echart_test4(req_matid, datax, data1);
      }, err => {
        console.log(err);
      })
    },

    async MDB_Query_flatness(req_matid, data) {
      const _this = this
      await axios({
        method: 'post',
        url: '/api/MDB_Query',
        data: JSON.stringify(
          {
            "coll_name": "datacollect622",
            "filter": {
              "extid": req_matid
            }
          }),
      }).then(res => {
        console.log(res.data);
        var data_2d = {}
        for (var i = 0; i < 40; i++) {
          var datas10 = []
          var channel_name = "c622_tcm_shape_channel" + (i + 1)
          datas10 = res.data.data[0].row[channel_name]
          data_2d[channel_name] = (datas10)
        }

        _this.query_2d_data(req_matid, data_2d);
      }, err => {
        console.log(err);
      })
    },
    echart_test4(mat_no, datax, data1) {
      console.log("test")
      // 基于准备好的dom，初始化echarts实例
      var myChart = Echarts.init(
        document.getElementById("main"),
        "light"
      );
      // 指定图表的配置项和数据
      var option = {
        title: {
          show: true,
          text: mat_no + "带钢板形二次拟合系数DS-OS ",
          textStyle: {
            color: "#fff",
          },
        },
        tooltip: {
          trigger: "axis",
          backgroundColor: "rgba(32, 33, 36,.7)",
          borderColor: "rgba(32, 33, 36,0.20)",
          borderWidth: 1,
          textStyle: {
            // 文字提示样式
            color: "#fff",
            fontSize: "12",
          },
        },
        grid: {
          left: "2%",
          right: "5%",
          bottom: "3%",
          containLabel: true,
        },
        color: ["#5470C6"],
        xAxis: {
          name: "长度[m]",
          type: "category",
          inverse: true,
          data: datax,
          axisLabel: {
            show: true,
            textStyle: {
              fontSize: 14, //更改坐标轴文字大小
            },
          },
          axisLine: {
            lineStyle: {
              color: "#fff", //改变坐标轴的颜色
            },
          },
        },
        yAxis: {
          // name: "",
          type: "value",
          max: "5",
          min: "-5",
          axisLabel: {
            formatter: "{value}",
            textStyle: {
              color: "#fff",
            },
          },
          nameTextStyle: {
            fontSize: 16,
          },
          axisLine: {
            lineStyle: {
              color: "#fff", //改变坐标轴的颜色
            },
          },
        },
        legend: {
          left: "right",
          textStyle: {
            fontSize: 14, //字体大小
            color: "#ffffff", //字体颜色
          },
        },
        series: [
          {
            name: "一次项系数(黄色)值越大，DS侧非对称浪形越大",
            data: data1,
            type: "line",
            smooth: true,
            color: "#FFFF00",
            symbolSize: "none",
          }
        ],
      };
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
      myChart.resize();
    },
    // 2D板形图
    query_2d_data(mat_no, datas10) {
      var need_x11 = []
      // for (
      //   var i = 0;
      //   i < datas10.c622_tcm_shape_channel11.length;
      //   i++
      // ) {
      //   need_x11.push(i + 1)
      // }
      
      for (var i = datas10.c622_tcm_shape_channel11.length; i >0; i--) {
        need_x11.push(i)
        }
      let res = []
      let max = ''
      Object.entries(datas10).forEach(([key, value]) => {
        const macthReq = /c622_tcm_shape_channel(\d+)$/.exec(key)
        if (!macthReq || value.every(i => i === 0)) return
        const index = Number(macthReq[1])
        max = Math.max(max, index)
        // for (i = 0; i < value.length; i++) {
        //   res.push([i + 1, index, value[i]])
        // }
        value.forEach((v, i) => {
          res.push([i + 1, index, v])
        })
      })
      // this.echartRes9 = res.sort((a, b) => a[0] - b[0])
      this.echartRes9_list = need_x11

      var myChart = Echarts.init(document.getElementById("flatnessmap_2d"), "light"); //将配置注入到html中定义的容器
      // prettier-ignore
      var days = [
        'OS_FL_C1',
        'FL_C2',
        'FL_C3',
        'FL_C4',
        'FL_C5',
        'FL_C6',
        'FL_C7',
        'FL_C8',
        'FL_C9',
        'FL_C10',
        'FL_C11',
        'FL_C12',
        'FL_C13',
        'FL_C14',
        'FL_C15',
        'FL_C16',
        'FL_C17',
        'FL_C18',
        'FL_C19',
        'FL_C20',
        'FL_C21',
        'FL_C22',
        'FL_C23',
        'FL_C24',
        'FL_C25',
        'FL_C26',
        'FL_C27',
        'FL_C28',
        'FL_C29',
        'FL_C30',
        'FL_C31',
        'FL_C32',
        'FL_C33',
        'FL_C34',
        'FL_C35',
        'FL_C36',
        'FL_C37',
        'FL_C38',
        'FL_C39',
        'DS_FL_C40'
      ]
      var option = {
        animation: false,
        title: {
          text: "带钢"+ mat_no + "板形2D图",
          textStyle: {
            color: "#ccc",
            fontStyle: "normal",
            fontWeight: "bold",
            fontFamily: "sans-serif",
            fontSize: 18,
          },
        },
        tooltip: {},
        grid: {
          left: "0",
          right: "5%",
          containLabel: true,
        },
        dataZoom: [
          {
            type: "inside",
            start: 0,
            end: 100,
          },
          {
            start: 0,
            end: 100,
          },
        ],
        xAxis: {
          type: "category",
          inverse: true,
          intercal: 50,
          boundaryGap: false,
          name: "米",
          axisLine: {
            lineStyle: {
              color: "#bdc0c7",
              width: 1, //这里是为了突出显示加上的
            },
          },
          nameTextStyle: {
            fontSize: 15,
            padding: [0, 0, 0, -10],
            color: "#ffffff",
          },
          axisPointer: {
            value: "1",
            lineStyle: {
              color: "#ff0640",
              opacity: 0.5,
              width: 2,
            },
            handle: {
              show: true,
              size: 20,
              margin: 40,
              color: "#ff0640",
            },
          },
          data: need_x11,
        },
        yAxis: {
          name: "通道",
          splitLine: {
            show: false,
          },
          axisLine: {
            lineStyle: {
              color: "#ffffff",
              width: 1, //这里是为了突出显示加上的
            },
          },
          nameTextStyle: {
            fontSize: 15,
            padding: [0, 0, 0, -10],
            color: "#ffffff",
          },
          type: "category",
          data: days,
        },
        legend: {
          left: "center",
          textStyle: {
            fontSize: 18, //字体大小
            color: "#ffffff", //字体颜色
          },
        },
        visualMap: {
          min: -10,
          max: 10,
          calculable: true,
          orient: "vertical",
          left: "right",
          top: "center",
          realtime: false,
          textStyle: {
            color: "#ffffff",
          },
          inRange: {
            color: [
              "#0000ff",
              "#00e3ff",
              "#00ffaa",
              "#aaff00",
              "#ffe400",
              "#ff0000",
            ],
          },
        },
        series: [
          {
            blurSize: 10,
            pointSize: 10, // 设置热力图上点的大小
            symbolSize: 200,
            // name: '带钢板形2D图',
            type: "heatmap",
            animation: false, // 是否开启动画
            sampling: "average", //降采样策略
            data: res,
            label: {
              normal: {
                show: false,
                color: "#fff",
                /*position: 'inner'*/
              },
            },
            lineStyle: {
              width: 3,
            },
            itemStyle: {
              //通常情况下：
              normal: {
                label: {
                  width: 2,
                  show: true,
                  position: "top",
                  color: "#fff",
                  fontSize: 12,
                },
              },
            },
            tooltip: {
              position: "top",
              backgroundColor: "rgba(0,0,0,0.5)",
              borderColor: "#333",
              borderWidth: 0,
              padding: 2,
              textStyle: {
                color: "#fff",
              },
              extraCssText:
                "box-shadow: 0 0 3px rgba(0, 0, 0, 0.1);font-weight:bold;",
              show: true,
              formatter: function (params) {
                return params.value[2];
              },
            },
          },
        ],
      };
      //使用刚指定的配置项和数据显示图表。
      // myChart.setOption(option, true)
      //清空画布，防止缓存
      myChart.clear();
      //使用刚指定的配置项和数据显示图表。mouseover
      myChart.setOption(option, true);
    },
  },
};
</script>
<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {

  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
