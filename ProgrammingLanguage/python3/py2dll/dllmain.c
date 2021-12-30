#include <Python.h>
#include <Windows.h>
#include "run.h"

extern __declspec(dllexport) int __stdcall _str_add(const char *a, const char *b)
{
    return PyLong_AsLong(str_add(PyUnicode_FromString(a), PyUnicode_FromString(b)));
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)
{
    switch (fdwReason)
    {
    case DLL_PROCESS_ATTACH:
        Py_Initialize();
        PyInit_run();
#dll初始化的时候调用，这是python3的写法，python2改成，initrun()。参见生成的run.h break;
    case DLL_PROCESS_DETACH:
        Py_Finalize();
        break;
    }
    return TRUE;
}