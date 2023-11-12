
import time
import multiprocessing

def factorize(number):
    factors = [i for i in range(1, number + 1) if number % i == 0]
    return factors

def parallel_factorize(*numbers):
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    results = pool.map(factorize, numbers)
    return results

if __name__ == '__main__':
    numbers = (128, 255, 99999, 10651060)

    # Measuring time for the synchronous version
    start_time = time.time()
    result_sync = [factorize(number) for number in numbers]
    end_time = time.time()
    print("Execution time of the synchronous version:", end_time - start_time)

    # Measuring time for a parallel version
    start_time = time.time()
    result_parallel = parallel_factorize(*numbers)
    end_time = time.time()
    print("Execution time of the parallel version:", end_time - start_time)















    # from multiprocessing import Pool, Array
    # import time
    # import sys
    #
    #
    # def modul_calculator(n):
    #     result = list()
    #     for i in range(1, n + 1):
    #         if n % i == 0:
    #             result.append(i)
    #     sys.exit()
    #     return result
    #
    # start = time.perf_counter()
    #
    # def factorize(numbers: list):
    #
    #     with Pool(len(numbers)) as pool:
    #         mapped = pool.map(modul_calculator, numbers)
    #
    #         # total_results.append(result)
    #     return mapped
    #
    #
    # a, b, c, d  = factorize([128, 255, 99999, 10651060])
    #
    # stop = time.perf_counter()
    #
    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    #
    # print(f'It took {stop-start}')







