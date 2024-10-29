ping(addressvalue,addressPortvalue);  //ip  port

function ping(ip,port) {
		  var img = new Image();
		  var start = new Date().getTime();
		  var flag = false;
		  var isCloseWifi = true;
		  var hasFinish = false;
		  img.onload = function() {
		    if ( !hasFinish ) {
		      flag = true;
		      hasFinish = true;
		      img.src = 'X:\\';
		      console.log('Ping ' + ip + ' success. ');
		    }
		  };
		  img.onerror = function() {
		    if ( !hasFinish ) {
		      if ( !isCloseWifi ) {
		        flag = true;
		        img.src = 'X:\\';
		        console.log('Ping ' + ip + ' success. ');
	        	var localAddressvalue=window.location.href;
	        	//跳转至快捷会场页面
	        	window.location.href="http://"+ip+":"+port+"/admin/login2.do?Ip="+returnCitySN["cip"]+"&localAddressvalue="+localAddressvalue;
		      } else {
		        console.log('network is not working!');
		      }
		      hasFinish = true;
		    }
		  };
		  setTimeout(function(){
		    isCloseWifi = false;
		  },2);
		  img.src = 'http://' + ip + '/' + start;
		  var timer = setTimeout(function() {
		    if ( !flag ) {
		      hasFinish = true;
		      img.src = 'X://';
		      flag = false ;
		      console.log('Ping ' + ip + ' fail. ');
        	//停留着编辑页面
        	document.getElementById("addresstipe").innerHTML="会议系统地址不在线,请联系管理人员!!!";
			document.getElementById("addresstipe").style.color="red";
			document.getElementById("addressId").focus();
		    }
		  }, 1500);
		}
