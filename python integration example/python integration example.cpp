#include <iostream>
#include <vector>
#include <string>
#include <iterator>

using namespace std;

class CHello
{
private:
    vector<wstring> m_vec;

public:
    void print()
    {
        vector<wstring>::iterator it;
        for (it = m_vec.begin(); it != m_vec.end(); it++)
        {
            wcout << (*it) << endl;
        }
    }

    void push_back(wstring s)
    {
        m_vec.push_back(s);
    }
};
extern "C" {
    __declspec(dllexport) CHello* CHello_new()
    {
        return new CHello();
    }

    __declspec(dllexport) void CHello_print(CHello * f)
    {
        f->print();
    }

    __declspec(dllexport) void CHello_push_back(CHello * f, wchar_t* s)
    {
        f->push_back(s);
    }

    __declspec(dllexport) wchar_t* print(wchar_t* s)
    {
        wcout << "get: " << s << endl;
        return s;
    }

    __declspec(dllexport) int* intarraytest()
    {
        static int r[3] = { 1,2,3 };
        return r;
    }
}