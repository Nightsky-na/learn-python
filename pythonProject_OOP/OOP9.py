def immutable_demo():
    # String and Integer are immutable object.
    n = 5
    print("id(n) = {}, n = {}".format(id(n), n))
    #  ที่ตั้งหน่วยความจำที่เก็บ 5 อยู่
    # id แรกก็จะเข้า garbage collection
    n = n + 4  # สร้างตัวใหม่
    print("id(n) = {}, n = {}".format(id(n), n))

    s = "rain"
    print("id(s) = {}, s = {}".format(id(s), s))
    s = s + "bow"
    print("id(s) = {}, s = {}".format(id(s), s))


def mutable_demo():
    #  String is mutable
    p = ["rain"]
    print("id(p) = {}, p = {}".format(id(p), p))
    p[0] = p[0] + "bow"
    print("id(p) = {}, p = {}".format(id(p), p))
    q = p
    print("id(p) = {}, p = {}\nid(q) = {}, q = {}".format(id(p), p, id(q), q))
    q.append("sunshine")
    print("id(p) = {}, p = {}\nid(q) = {}, q = {}".format(id(p), p, id(q), q))


if __name__ == '__main__':
    immutable_demo()
    print("\n")
    mutable_demo()
