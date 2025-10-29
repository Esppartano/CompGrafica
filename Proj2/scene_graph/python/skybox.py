from OpenGL.GL import *
from shape import *
from sphere import Sphere
import glm

class SkyBox(Shape):
  def __init__(self):
    # reuse high-resolution sphere geometry with equirectangular UVs
    # we render it from the inside as a background
    self._sphere = Sphere(nstack=64, nslice=64)

  def Draw(self, st):
    # draw centered at the camera position so it appears infinitely far
    camera = st.GetCamera()
    origin = glm.vec4(0,0,0,1)
    peye = glm.vec3(glm.inverse(camera.GetViewMatrix()) * origin)
    M = glm.translate(glm.mat4(1), peye)
    st.PushMatrix()
    st.LoadMatrix(M)
    st.LoadMatrices()
    glDepthMask(GL_FALSE)
    # disable culling so inside of sphere is visible
    glDisable(GL_CULL_FACE)
    self._sphere.Draw(st)
    glEnable(GL_CULL_FACE)
    glDepthMask(GL_TRUE)
    st.PopMatrix()