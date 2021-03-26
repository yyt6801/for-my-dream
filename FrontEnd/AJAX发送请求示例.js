$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:8087/service_bkgy/webservice/sendMessage',
			dataType:"json",
			headers:{'Content-Type':'application/json;charset=utf8'},
			data:JSON.stringify(
						{
							"msgList":[
								{
									"id": "MSG1997",
									"timeout": 3,
									"reply": true,
									"data": [
										{
											CoilNo:$scope.COIL_ID,
											nextcoilno:"dskljfaljflalkjsadfjasdfjafdlaj",
										}
									]
								}
							]
						}),
			success: function (res) {
				console.log(res);
			},
		});


		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:8087/service_bkgy/common/findData',
			dataType:"json",
			headers:{'Content-Type':'application/json;charset=utf8'},
			data:JSON.stringify({
				        "key":"calcpc_res" ,
				        "list":[
				        ]
					}),
			success: function (res) {
				console.log(res);
			},
		});




		//用getHmiData获取中间件内部变量值
		$.ajax({
			type: 'POST',
			url: 'http://192.168.237.130:8087/service_bkgy/webservice/getHmiData',
			dataType:"json",
			headers:{'Content-Type':'application/json;charset=utf8'},
            crossDomain: true,
			data:JSON.stringify({
                            msgs: [],
							tags: [
								{name: en_Tag001, ts: '0'},
								{name: en_Tag002, ts: "0"},
							]
					}),
			success: function (res) {
				console.log(res);
			},
		});

				
$.ajax({
	type: "GET",
	url: "http://127.0.0.1:8000/get_pcdp_record?recordname=INFCE1",
	contentType: 'application/json;charset=utf-8', //设置请求头信息
	dataType: "json",
	success: function (res) {
		console.log(res);
	},
	error: function (result) {
		errorToast(result.msg);
	}
});