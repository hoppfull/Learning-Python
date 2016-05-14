import OpenGL.GL as GL
import OpenGL.GL.shaders as GL_shaders

def loadShader(vs, fs):
    # Load vertex shader file and compile:
    with open(vs, 'r') as vs_file:
        VERTEX_SHADER = GL_shaders.compileShader(
            vs_file.read(),
            GL.GL_VERTEX_SHADER)
    del vs_file # Delete file object, good programming practice
    # Load fragment shader file and compile:
    with open(fs, 'r') as fs_file:
        FRAGMENT_SHADER = GL_shaders.compileShader(
            fs_file.read(),
            GL.GL_FRAGMENT_SHADER)
    del fs_file # Delete file object, good programming practice
    # Compile and return shader program:
    return GL_shaders.compileProgram(VERTEX_SHADER, FRAGMENT_SHADER)

##TODO: Create a model loader and a texture loader!