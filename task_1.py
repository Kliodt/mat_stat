import numpy as np
import matplotlib.pyplot as plt

# биномиальное распределение
m = 4
th = 1/5

# объемы выборок
volumes = [100, 1000, 3000]

# тестовое количество выборок каждого объема
number_of_samples_tests = [50, 100, 1000]

rng = np.random.default_rng()

fig = plt.figure(figsize=(10, 6))
graph_pos = 0
for number_of_samples in number_of_samples_tests: # разное количество тестовых выборок
    graph_pos += 1
    sp = fig.add_subplot(1, len(number_of_samples_tests), graph_pos)

    x_avg = []
    x_disp = []
    x_out_of_range = []
    for n in volumes: # разные объемы выборок
        th_diff = []

        for i in range(number_of_samples):
            seq = rng.binomial(m, th, size=n)
            th_estimation = sum(seq)/(n*m)
            th_diff.append(th_estimation - th)

        # выборочные характеристики
        # выборочное среднее
        x_avg.append(1/n * sum(th_diff))

        # выборочная дисперсия
        x_disp.append(1/n * sum(map(lambda x: (x-x_avg[-1])**2, th_diff)))

        # отличаются больше чем на заданный порог
        x_out_of_range.append(sum([1 if abs(val) > 0.01 else 0 for val in th_diff]))

        # построение гистограммы
        sp.hist(th_diff, alpha=0.7)
    
    sp.set_title(f"Тестовых выборок: {number_of_samples}")
    sp.legend(volumes, title="Объём")
    sp.set_xlabel("Смещение")
    sp.set_ylabel("Частота")
    sp.text(0.5,-0.25, f"среднее выб-ное | выб-ная дисперсия | вылеты\n{"\n".join([str(round(x_avg[i], 8)) + " | " 
                                                                                + str(round(x_disp[i], 8)) + " | " 
                                                                                + str(x_out_of_range[i] / number_of_samples) 
                                                                                for i in range(len(x_avg))])}", 
            size=8, ha="center", transform=sp.transAxes)

plt.subplots_adjust(bottom=0.2)
plt.show()