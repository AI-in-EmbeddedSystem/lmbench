# org
README for lmbench 2alpha8 net release.

To run the benchmark, you should be able to say:

	cd src
	make results

If you want to see how you did compared to the other system results
included here, say

	make see

Be warned that many of these benchmarks are sensitive to other things
being run on the system, mainly from CPU cache and CPU cycle effects.
So make sure your screen saver is not running, etc.

It's a good idea to do several runs and compare the output like so

	make results
	make rerun
	make rerun
	make rerun
	cd Results && make LIST=<your OS>/*

If your os is euler or centos, please Uncomment line 250 and 251;

If you want to run the benchmark in loongarch , you just need to say:

	make results OS=mips64el


# compiling for aarch64
```bash
# make release version
cd src && make lmbench OS=aarch64 CC=aarch64-linux-gnu-gcc LDFLAGS=--static

# make w/systrace collecting version
cd src && make lmbench OS=aarch64 CC=aarch64-linux-gnu-gcc LDFLAGS=--static SYSTRACE=1

# make real bandwidth print version
cd src && make lmbench OS=aarch64 CC=aarch64-linux-gnu-gcc LDFLAGS=--static PRINT_ACCURATE_RESULT=1

# make debug version opening debug print
cd src && make lmbench OS=aarch64 CC=aarch64-linux-gnu-gcc LDFLAGS=--static DEBUG=1
```
# debug for systrace (only for bw_mem rd case)
```bash
# open tracing_mark_write and trace switch
echo 'trace_printk' > /sys/kernel/tracing/trace_options
echo 'markers' > /sys/kernel/tracing/trace_options
echo 1 > /sys/kernel/tracing/tracing_on

# 使用ftrace验证是否有输出（有输出，表明systrace log加入成功）
cat /sys/kernel/tracing/trace_pipe | grep tracing_mark_write

# 在其他shell窗口执行，
./bw_mem_systrace -P 8  1m rd

# 抓住sysrace，使用scripts/perfetto.sh，在PC侧执行
cd scripts && ./perfetto.sh
```
