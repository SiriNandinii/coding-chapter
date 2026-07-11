from typing import List

class SegmentTree:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (self.n * 4)
        self.length = [0] * (self.n * 4)

    def update(self, node, l, r, ql, qr, val):
        if ql >= r or qr <= l:
            return

        if ql <= l and r <= qr:
            self.count[node] += val
        else:
            mid = (l + r) // 2
            self.update(node * 2, l, mid, ql, qr, val)
            self.update(node * 2 + 1, mid, r, ql, qr, val)

        if self.count[node] > 0:
            self.length[node] = self.xs[r] - self.xs[l]
        elif r - l == 1:
            self.length[node] = 0
        else:
            self.length[node] = (
                self.length[node * 2]
                + self.length[node * 2 + 1]
            )

    def covered(self):
        return self.length[1]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = []

        for x, y, l in squares:
            x1 = x
            x2 = x + l

            events.append((y, 1, x1, x2))
            events.append((y + l, -1, x1, x2))

            xs.append(x1)
            xs.append(x2)

        xs = sorted(set(xs))
        x_id = {x: i for i, x in enumerate(xs)}

        events.sort()

        st = SegmentTree(xs)

        strips = []
        total_area = 0

        prev_y = events[0][0]
        i = 0

        while i < len(events):
            y = events[i][0]

            if y > prev_y:
                covered = st.covered()
                dy = y - prev_y
                area = covered * dy

                strips.append((prev_y, y, covered, area))
                total_area += area

            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                st.update(
                    1,
                    0,
                    st.n,
                    x_id[x1],
                    x_id[x2],
                    typ
                )
                i += 1

            prev_y = y

        target = total_area / 2.0
        prefix = 0.0

        for y1, y2, covered, area in strips:
            if prefix + area >= target:
                return y1 + (target - prefix) / covered

            prefix += area

        return 0.0