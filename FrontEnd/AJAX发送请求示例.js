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