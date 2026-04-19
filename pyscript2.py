from random import randint as rnd
from time import sleep as slp

loadlist = "E:/root/scl/os/core.sys - E:/root/scl/os/init.cfg - E:/root/scl/os/boot.lnx - E:/root/scl/os/alpha.bin - E:/root/scl/os/kernel.x - E:/root/scl/os/memload.dll - E:/root/scl/os/exec.run - E:/root/scl/os/cache.tmp - E:/root/scl/os/render.mod - E:/root/scl/os/input.dev - E:/root/scl/os/output.dev - E:/root/scl/os/syscall.api - E:/root/scl/os/graph.vtx - E:/root/scl/os/shell.cmd - E:/root/scl/os/netstack.drv - E:/root/scl/os/crypto.key - E:/root/scl/os/driver.hdl - E:/root/scl/os/pipe.str - E:/root/scl/os/frame.buf - E:/root/scl/os/event.hook - E:/root/scl/os/corelink.map - E:/root/scl/os/scheduler.tsk - E:/root/scl/os/thread.mgr - E:/root/scl/os/debug.log - E:/root/scl/os/stack.mem - E:/root/scl/os/alloc.tbl - E:/root/scl/os/fsys.img - E:/root/scl/os/backup.arc - E:/root/scl/os/mount.pt - E:/root/scl/os/user.dat - E:/root/scl/os/root.sec - E:/root/scl/os/token.gen - E:/root/scl/os/session.id - E:/root/scl/os/proc.lst - E:/root/scl/os/zone.map - E:/root/scl/os/clock.sys - E:/root/scl/os/time.drv - E:/root/scl/os/audio.ch - E:/root/scl/os/video.ch - E:/root/scl/os/io.ctrl - E:/root/scl/os/power.mgr - E:/root/scl/os/bios.int - E:/root/scl/os/firm.hex - E:/root/scl/os/flash.rom - E:/root/scl/os/config.sys - E:/root/scl/os/cache2.tmp - E:/root/scl/os/ramdisk.img - E:/root/scl/os/virt.mem - E:/root/scl/os/swap.sec - E:/root/scl/os/monitor.exe - E:/root/scl/os/gui.pkg - E:/root/scl/os/theme.res - E:/root/scl/os/font.vec - E:/root/scl/os/lang.dat - E:/root/scl/os/input2.dev - E:/root/scl/os/output2.dev - E:/root/scl/os/stream.buf - E:/root/scl/os/net.api - E:/root/scl/os/dns.tbl - E:/root/scl/os/http.mod - E:/root/scl/os/socket.if - E:/root/scl/os/firewall.cfg - E:/root/scl/os/auth.sec - E:/root/scl/os/encrypt.mod - E:/root/scl/os/decrypt.mod - E:/root/scl/os/packet.buf - E:/root/scl/os/route.map - E:/root/scl/os/gateway.dev - E:/root/scl/os/port.lst - E:/root/scl/os/scan.log - E:/root/scl/os/virus.sig - E:/root/scl/os/sandbox.env - E:/root/scl/os/isolate.mod - E:/root/scl/os/update.pkg - E:/root/scl/os/patch.diff - E:/root/scl/os/recovery.img - E:/root/scl/os/safe.boot - E:/root/scl/os/checksum.md5 - E:/root/scl/os/hash.sha - E:/root/scl/os/license.key - E:/root/scl/os/reg.dat - E:/root/scl/os/serial.num - E:/root/scl/os/temp.buf - E:/root/scl/os/queue.lst - E:/root/scl/os/task.run - E:/root/scl/os/job.exec - E:/root/scl/os/plan.cfg - E:/root/scl/os/event2.hook - E:/root/scl/os/sysmon.exe - E:/root/scl/os/trace.log - E:/root/scl/os/report.txt - E:/root/scl/os/error.log - E:/root/scl/os/fault.dump - E:/root/scl/os/alert.msg - E:/root/scl/os/notify.sys - E:/root/scl/os/service.mgr - E:/root/scl/os/daemon.run - E:/root/scl/os/worker.thr - E:/root/scl/os/controller.ai - E:/root/scl/os/logic.unit - E:/root/scl/os/core2.sys - E:/root/scl/os/expand.mod - E:/root/scl/os/linker.bin - E:/root/scl/os/compile.obj - E:/root/scl/os/runtime.env - E:/root/scl/os/meta.inf - E:/root/scl/os/overlay.pkg - E:/root/scl/os/plugin.ext - E:/root/scl/os/module.dep - E:/root/scl/os/graph2.vtx - E:/root/scl/os/fx.render - E:/root/scl/os/light.map"
load = loadlist.split(" - ")

k = False
while not k:
    p = False
    while not p:
        inp = input("START LOADING SCLOS?(Y/N)")
        if inp == "y":
            lastf = 0
            l = 0
            lastl = 0
            a = 0
            f = 0
            o = False
            s = 0
            s += rnd(0, 9)
            s = str(s)
            for _ in range(7):
                s = f"{s}{rnd(0, 9)}"
            s = int(s)/100000000
            print("\nSCLOS LOADING...")
            while l < 100:
                if s >= 0.5:
                    f += rnd(-3, 5)/100
                elif s >= 0.25:
                    f += rnd(-4, 5)/100
                elif s >= 0.05:
                    f += rnd(-5, 6)/100
                else:
                    f += rnd(-6, 6)/100
                if f < 0:
                    f = 0
                a += rnd(1, 5)/10
                if f >= 1:
                    print("LOADING FAIL: UNEXPECTED ERROR")
                    break
                elif f >= 0.9 and lastf != 0.9:
                    lastf = 0.9
                    print("CRITICAL ERROR: KERNEL RESPONSE TIMEOUT")
                elif f >= 0.7 and lastf != 0.7:
                    lastf = 0.7
                    print("UNSTABLE STATUS: THREAD DESYNCHRONIZATION DETECTED")
                elif f >= 0.5 and lastf != 0.5:
                    lastf = 0.5
                    print("ERROR WARNING: HIGH LATENCY (MEMORY.DLL)")
                if a >= 1:
                    l += rnd(30, 100)/100
                else:
                    l += rnd(1, 30)/100
                if l > 100:
                    l = 100
                if l == 100:
                    o = True
                print(f"{load[rnd(0, len(load)-1)]: <32}|{str(l)[:5]}%")
                print(f"{f'_debug fail: {f}%': <32}|{str(l)[:5]}%")
                print(f"{f'_debug seed: {s}': <32}|{str(l)[:5]}%")
                if lastf == 0:
                    slp(rnd(5, 20)/1000)
                elif lastf == 0.5:
                    slp(rnd(3, 5)/100)
                elif lastf == 0.7:
                    slp(rnd(5, 20)/100)
                elif lastf == 0.9:
                    slp(rnd(3, 5)/10)
            print("\nSCLOS LOADED")
            if o:
                p = True
        elif inp == "n":
            print("LOADING SCLOS CANCELLED")
            k = True
        else:
            print("USE Y OR N TO ANSWER")
    slp(1)
    print("\n")
print("programm ended")