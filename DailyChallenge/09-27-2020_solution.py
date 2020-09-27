class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = {}
        for e, v in zip(equations, values):
            e0, e1 = e[0], e[1]
            if e0 not in d:
                d[e0] = {}
            if e1 not in d[e0]:
                d[e0][e1] = v
            if e1 not in d:
                d[e1] = {}
            if e0 not in d[e1]:
                d[e1][e0] = 1/v

        answers = []

        for query in queries:
            q0, q1 = query[0], query[1]
            if q0 not in d or q1 not in d:
                answers.append(-1.0)
                continue
            if q0 == q1:
                answers.append(1)
                continue

            seen = set()
            answer = -1.0
            queue = [(x, d[q0][x]) for x in d[q0].keys()]
            while queue:
                k,v = queue.pop()
                if k == q1:
                    answer = v
                    break
                seen.add(k)
                queue.extend([(x,d[k][x]*v) for x in d[k].keys() if x not in seen])
            answers.append(answer)

        return answers
