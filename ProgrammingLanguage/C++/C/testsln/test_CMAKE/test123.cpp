#include "mdwlib.h"
//需添加 项目属性 -> VC++目录 ->
//需添加 预处理器 _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS    _CRT_SECURE_NO_WARNINGS
//项目属性 -> 配置属性 -> C/C++ -> 代码生成 -> 运行库   设置为 多线程调试(/ MTd)

int main(int argc, char* argv[])
{
	Message			Msg;
	int				ret;

	ALARM(AL_INFO, 1002, true, "test_pro_using_vs2015程序启动");

	//初始化COM库，中间件库函数需要
	CoInitialize(NULL);

	//清空消息队列
	MakeEmpty();
	MDW_SYS_INFO info;
	GetMdwSysInfo(&info);

	TIMER_DATA timer;
	timer.Elapse = 10000;//每十秒监测开卷机是否有新卷上线
	AddTimer(2012, CycleType, timer);
	
	int x = 0;

	while (ret = Msg.Receive())
	{
		//接收消息出错
		if (ret <= 0)
		{
			Sleep(1000);
			continue;
		}
		switch (Msg.Id())
		{
		case EVENT_TIMER_ON:
			if (Msg.Param(L_PARAM1) == 2012)
			{
				//获取中间件内部变量
				int bianliang = TAG("bianliang");
				ALARM(AL_INFO, 8210, "bianliang值为%d", bianliang);
				TAG("bianliang") = 12345;
				ALARM(AL_INFO, 8210, "修改bianliang值OK!!!");

				float buff = 0;//第x个纠偏辊上的CPC纠偏缸位置数据
				buff = float(TAG("Tag001"));//实时各CPC纠偏缸位置数据
				ALARM(AL_INFO, 8210, "Tag001值为%f", buff);

				double d = TAG("Tag002");
				ALARM(AL_INFO, 8210, "Tag002值为%f", buff);

				char aaa[20];
				memset(aaa, 0x00, sizeof(aaa));
				strcpy(aaa, (const char*)(FormatString)TAG("aaa"));
				ALARM(AL_INFO, 8210, "Tag002值为%s", aaa);

				//Records COIL_INFO_Rec;
				//COIL_INFO_Rec.Clear();//初始化赋值时需要这样定义，如果不是赋值，只是读取的话，不需要Clear()
				//char* mat_no_old[20];
				//Records COIL_m_Rec = TAG("testrec");//只获取记录集中数据,直接=  ，不需要Clear()
				//for (int x = 0; x < 10; x++)
				//{
				//	strcpy(mat_no_old[x], (const char*)FormatString(COIL_m_Rec[x]["CPC8_ROLL1_POS"]));
				//	printf("testrec-%d-%s",x, mat_no_old[x]);
				//}


			}
			if (Msg.Param(L_PARAM1) == 2013)
			{

			}
			break;


		case 2013://画面点击事件开始取第x米处对应的板型
			 x = Msg.Param(L_PARAM1);//x为点击的第几根辊,辊子的编号传过来 2,4,9
			ALARM(AL_INFO, 8231, "画面点击事件!编号为%d", x);

			TAG("click_cpc_no") = x;
			//click_asc(x);

			break;
		case 1113://test开始事件			

			break;
		default:
			ALARM(AL_DEBUG, 1043,"zzz");
			break;
		}
	}


	CoUninitialize();

	ALARM(AL_ERROR, 1002, true, "test_pro_using_vs2015程序退出");

	return 0;
}