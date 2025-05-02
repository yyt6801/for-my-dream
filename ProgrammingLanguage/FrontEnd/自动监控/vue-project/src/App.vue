<template>
  <div class="greetings">
    <div id="main">
      <input type="button" value="监控所有api" @click="monitor()" />
      <div v-if="results.length">
        <h2>查询结果</h2>
        <ul>
          <li v-for="(result, index) in results" :key="index">
            <pre>{{ result }}</pre>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      config: 
         [{
          id:"config_test1",
          db: "ORAINS",
          sql: "select * from (select t.coilno,t.create_time,t.prodend from tb_tcm2_pdo t order by t.create_time desc )where rownum = 1"
        },
        {
          id:"config_test2",
          db: "mdb",
          sql: "select * from pltcm_asc_result where extid = 'C231050020'"
        },
        {
          id:"config_test3",
          db: "mdb",
          sql: "select * from pltcm_asc_result where extid = 'C231050020'"
        },
        {
          id:"config_test4",
          db: "mdb",
          sql: "select * from pltcm_asc_result where extid = 'C231050020'"
        }
        ],
      results: []
    };
  },
  methods: {
    async monitor() {
      this.results = [];
      for (const config of this.config) {
        try {
          const response = await axios.post('/api/DB_Query', {
            sql: config.sql,
            db: config.db
          });
          this.results.push(response.data);
        } catch (error) {
          console.error('Error executing SQL:', error);
        }
      }
    },
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
    }
  },
};
</script>
