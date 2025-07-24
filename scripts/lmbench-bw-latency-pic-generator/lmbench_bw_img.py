import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_latency_vs_size(folder_path, output_image_path='bw_rd.png'):
    # 设置图片尺寸，这里宽度为 10 英寸，高度为 6 英寸
    plt.figure(figsize=(12, 6))


    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                try:
                    # 读取 CSV 文件
                    df = pd.read_csv(file_path)
                    size = df['blocksize']
                    bw = df['Bandwidth']

                    # 绘制线条图，使用文件名作为图例
                    plt.plot(size, bw, label=file)
                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {e}")

    # 设置图表标题和坐标轴标签
    plt.title('Bandwidth rd')
    plt.xlabel('block size')
    plt.ylabel('Bandwidth(MB/s)')

    # 设置 Y 轴范围，最小值自动确定，最大值设置为 180000
    plt.ylim(top=180000)

    # 显示图例
    plt.legend(loc='upper right')

    # 保存图片
    plt.savefig(output_image_path)

    # 关闭图表
    plt.close()

    print(f"图片已保存至 {output_image_path}")


# 使用示例
if __name__ == "__main__":
    folder_path = r'bw_data'  # 替换为实际的 CSV 文件路径
    plot_latency_vs_size(folder_path)

