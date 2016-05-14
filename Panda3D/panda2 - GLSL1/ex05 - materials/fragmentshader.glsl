#version 330

//Texturing:
uniform sampler2D p3d_Texture0;
in vec2 mytexcoord0;

//Material:
uniform struct {
    vec4 ambient;
    vec4 diffuse;
    vec4 emission;
    vec3 specular;
    float shininess;
} p3d_Material;

//Input from main program:
uniform vec3 dlight1_pos;
/* Position of directional light 1, assuming
it's pointing in towards the center of the scene */

void main(){
    vec4 textureColor = vec4( texture2D(p3d_Texture0, mytexcoord0) ) * p3d_Material.diffuse;
    gl_FragColor = textureColor;
}