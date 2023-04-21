from threading import Thread
import _xxsubinterpreters as subinterpreters



def bench_subinterpreters():
    # Code to launch specific model
    def _spawn_sub():
        for _ in range(100):
            sid = subinterpreters.create()
            subinterpreters.run_string(sid, "")
            subinterpreters.destroy(sid)

    
    t = Thread(target=_spawn_sub)
    t.start()
    t.join()


if __name__ == "__main__":
    bench_subinterpreters()
