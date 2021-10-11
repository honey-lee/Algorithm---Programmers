def solution(sizes):
    m_w, m_h = 0, 0
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    for i in range(len(sizes)):
        if sizes[i][0] >= m_w:
            m_w = sizes[i][0]
        if sizes[i][1] >= m_h:
            m_h = sizes[i][1]

    return m_w * m_h