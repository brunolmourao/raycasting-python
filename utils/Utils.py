import numpy as np


def camera_init_(view, l_at, v_up):
    k = view - l_at
    kc = k / np.linalg.norm(k)

    v = v_up - view
    i = np.cross(v, kc)
    ic = i / np.linalg.norm(i)

    jc = np.cross(kc, ic)

    """
    # cam->world
    ic = np.append(ic, [0])
    jc = np.append(jc, [0])
    kc = np.append(kc, [0])
    vi = np.append(view, [1])
    """

    # world->cam
    ic = np.append(ic, [-np.dot(view, ic)])
    jc = np.append(jc, [-np.dot(view, jc)])
    kc = np.append(kc, [-np.dot(view, kc)])
    vi = np.array([0, 0, 0, 1])

    cam = ic
    cam = np.vstack((cam, jc))
    cam = np.vstack((cam, kc))
    cam = np.vstack((cam, vi))
    # cam = np.transpose(cam)

    return cam

def calcula_cor(obj, f_lum):
    pass