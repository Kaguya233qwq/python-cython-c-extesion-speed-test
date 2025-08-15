import timeit

import c_speed_test
import cython_speed_test


# 原生Python实现
def native_python_compute(n: int) -> float:
    total_sum = 0.0
    for i in range(n):
        total_sum += i * 1.01
    return total_sum


def run_comparison():

    N = 50_000_000
    RUNS = 3

    print(f"开始性能对比测试...")
    print(f"计算任务: sum(i * 1.01 for i in range({N}))")
    print(f"每个测试运行 {RUNS} 次取平均值。\n")

    # --- 原生 Python ---
    py_timer = timeit.Timer(lambda: native_python_compute(N))
    py_time = min(py_timer.repeat(repeat=RUNS, number=1))
    print(f"原生 Python: {py_time:.6f} 秒")

    # --- C 扩展 ---
    c_timer = timeit.Timer(lambda: c_speed_test.compute(N))
    c_time = min(c_timer.repeat(repeat=RUNS, number=1))
    print(f"C 扩展:      {c_time:.6f} 秒")

    # --- Cython ---
    cython_timer = timeit.Timer(lambda: cython_speed_test.compute(N))
    cython_time = min(cython_timer.repeat(repeat=RUNS, number=1))
    print(f"Cython:   {cython_time:.6f} 秒")

    print("\n--- 性能提升对比 ---")
    print(f"C 扩展相对于 Python 提速: {py_time / c_time:.2f} 倍")
    print(f"Cython 相对于 Python 提速: {py_time / cython_time:.2f} 倍")

    # --- 验证结果是否一致 ---
    print("\n--- 结果验证 ---")
    res_py = native_python_compute(1000)
    res_c = c_speed_test.compute(1000)
    res_cy = cython_speed_test.compute(1000)
    print(f"Python 结果: {res_py}")
    print(f"C 结果:      {res_c}")
    print(f"Cython 结果: {res_cy}")
    assert abs(res_py - res_c) < 1e-9 and abs(res_py - res_cy) < 1e-9
    print("所有模块计算结果一致")


if __name__ == "__main__":
    run_comparison()
