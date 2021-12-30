#include "mdwlib.h"
//����� ��Ŀ���� -> VC++Ŀ¼ ->
//����� Ԥ������ _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS    _CRT_SECURE_NO_WARNINGS
//��Ŀ���� -> �������� -> C/C++ -> �������� -> ���п�   ����Ϊ ���̵߳���(/ MTd)

int main(int argc, char* argv[])
{
	Message			Msg;
	int				ret;

	ALARM(AL_INFO, 1002, true, "test_pro_using_vs2015��������");

	//��ʼ��COM�⣬�м���⺯����Ҫ
	CoInitialize(NULL);

	//�����Ϣ����
	MakeEmpty();
	MDW_SYS_INFO info;
	GetMdwSysInfo(&info);

	TIMER_DATA timer;
	timer.Elapse = 10000;//ÿʮ���⿪����Ƿ����¾�����
	AddTimer(2012, CycleType, timer);
	
	int x = 0;

	while (ret = Msg.Receive())
	{
		//������Ϣ����
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
				//��ȡ�м���ڲ�����
				int bianliang = TAG("bianliang");
				ALARM(AL_INFO, 8210, "bianliangֵΪ%d", bianliang);
				TAG("bianliang") = 12345;
				ALARM(AL_INFO, 8210, "�޸�bianliangֵOK!!!");

				float buff = 0;//��x����ƫ���ϵ�CPC��ƫ��λ������
				buff = float(TAG("Tag001"));//ʵʱ��CPC��ƫ��λ������
				ALARM(AL_INFO, 8210, "Tag001ֵΪ%f", buff);

				double d = TAG("Tag002");
				ALARM(AL_INFO, 8210, "Tag002ֵΪ%f", buff);

				char aaa[20];
				memset(aaa, 0x00, sizeof(aaa));
				strcpy(aaa, (const char*)(FormatString)TAG("aaa"));
				ALARM(AL_INFO, 8210, "Tag002ֵΪ%s", aaa);

				//Records COIL_INFO_Rec;
				//COIL_INFO_Rec.Clear();//��ʼ����ֵʱ��Ҫ�������壬������Ǹ�ֵ��ֻ�Ƕ�ȡ�Ļ�������ҪClear()
				//char* mat_no_old[20];
				//Records COIL_m_Rec = TAG("testrec");//ֻ��ȡ��¼��������,ֱ��=  ������ҪClear()
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


		case 2013://�������¼���ʼȡ��x�״���Ӧ�İ���
			 x = Msg.Param(L_PARAM1);//xΪ����ĵڼ�����,���ӵı�Ŵ����� 2,4,9
			ALARM(AL_INFO, 8231, "�������¼�!���Ϊ%d", x);

			TAG("click_cpc_no") = x;
			//click_asc(x);

			break;
		case 1113://test��ʼ�¼�			

			break;
		default:
			ALARM(AL_DEBUG, 1043,"zzz");
			break;
		}
	}


	CoUninitialize();

	ALARM(AL_ERROR, 1002, true, "test_pro_using_vs2015�����˳�");

	return 0;
}