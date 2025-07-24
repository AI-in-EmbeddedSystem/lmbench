#! /bin/sh
cur_dateTime="`date +%Y%m%d%H%M%S`"
echo ${cur_dateTime}
adb  shell "echo 0 > /sys/kernel/tracing/tracing_on"
adb  shell perfetto -o /data/misc/perfetto-traces/trace_file.perfetto-trace -t 60s sched freq idle am wm gfx view binder_driver hal dalvik camera input res memory
adb  pull /data/misc/perfetto-traces/trace_file.perfetto-trace ./${cur_dateTime}.perfetto-trace
