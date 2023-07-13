class hello_world:
    class hello:
        class h:
            class e:
                class l:
                    class l:
                        class o:
                            def hello():
                                return "h" + "e" + "l" + "l" + "o"
    class world:
        class w:
            class o:
                class r:
                    class l:
                        class d:
                            def world():
                                return "w" + "o" + "r" + "l" + "d"
    def hello_world():
        return hello_world.hello.h.e.l.l.o.hello() + hello_world.world.w.o.r.l.d.world()

print(hello_world.hello_world())