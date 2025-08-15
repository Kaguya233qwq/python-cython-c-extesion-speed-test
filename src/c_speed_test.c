#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* compute_c(PyObject* self, PyObject* args) {
    long n;
    // 解析从Python传入的参数
    if (!PyArg_ParseTuple(args, "l", &n)) { //
        return NULL;
    }

    double total_sum = 0.0;
    for (long i = 0; i < n; i++) {
        total_sum += (double)i * 1.01;
    }

    // 将C的double类型结果转换回Python的Float对象并返回
    return PyFloat_FromDouble(total_sum);
}

// 定义模块中的方法
static PyMethodDef SpeedTestMethods[] = {
    {"compute", compute_c, METH_VARARGS, "A computationally intensive function in C."},
    {NULL, NULL, 0, NULL}
};

// 定义模块本身
static struct PyModuleDef c_speed_test_module = {
    PyModuleDef_HEAD_INIT,
    "c_speed_test",
    "A C extension for speed testing.",
    -1,
    SpeedTestMethods
};

// 模块的初始化函数
PyMODINIT_FUNC PyInit_c_speed_test(void) {
    return PyModule_Create(&c_speed_test_module);
}