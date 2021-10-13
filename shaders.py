import numpy as np
import random
import algebruh as al
def flat(render, **kwargs):
    # Iluminacion se calcula por primitiva

    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    triangleNormal = kwargs['triangleNormal']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    dirLight = np.array(render.directional_light)
    intensity = al.dot(triangleNormal, -dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def gourad(render, **kwargs):
    # Iluminacion por vertice, se interpola
    # la iluminacion por cada pixel
    
    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    dirLight = np.array(render.directional_light)
    intensityA = al.dot(nA, -dirLight)
    intensityB = al.dot(nB, -dirLight)
    intensityC = al.dot(nC, -dirLight)

    intensity = intensityA *u + intensityB *v + intensityC *w
    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def phong(render, **kwargs):
    # Iluminacion por pixel
    
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = np.array(render.directional_light)
    intensity = al.dot(normal, -dirLight)

    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def unlit(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    return r, g, b

def tooned(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= (texColor[0])/ 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = np.array(render.directional_light)
    intensity = al.dot(normal, -dirLight)

    if intensity > 0.9:
        
            
        b*= (texColor[0]+20)/ 255
        if b>255:
            b=255
        b*=1
        g*= 0.5
        r*= 1
    elif intensity > 0.7:
                    
        b*= (texColor[0]+20)/ 255
        if b>255:
            b=255
        b*=0.8
        g*= 0.6
        r*= 0.6
    elif intensity > 0.6:
                
        b*= 0.7
        g*= 0.5
        r*= 0.5
        
    elif intensity > 0.4:
        r*= (texColor[2]+50)/ 255
        if r>255:
            r=255
        
        g*= 0.04
        b*= 0.04
        r*=0.6
    else:
        r*= (texColor[2]+100)/ 255
        if r>255:
            r=255
        b=r
        g*= 0.3
        b*= 0.3
        r*=0.5



    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0
def tuolf(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= (texColor[0])/ 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = np.array(render.directional_light)
    intensity = al.dot(normal, -dirLight)

    if intensity > 0.9:
        
            
        b*= (texColor[0]+20)/ 255
        if b>255:
            b=255
        b*=1
        g*= 0.5
        r*= 1
        m=g
        g=r
        r=m
    elif intensity > 0.7:
                    
        b*= (texColor[0]+20)/ 255
        if b>255:
            b=255
        b*=0.8
        g*= 0.6
        r*= 0.6
        m=g
        g=r
        r=m
    elif intensity > 0.6:
                
        b*= 0.7
        g*= 0.5
        r*= 0.5
        m=g
        g=r
        r=m
        
    elif intensity > 0.4:
        r*= (texColor[2]+50)/ 255
        if r>255:
            r=255
        
        g*= 0.04
        b*= 0.04
        r*=0.6
        m=g
        g=r
        r=m
    else:
        r*= (texColor[2]+100)/ 255
        if r>255:
            r=255
        b=r
        g*= 0.3
        b*= 0.3
        r*=0.5
        m=g
        g=r
        r=m



    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0
def tumbro(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= (texColor[0])/ 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = np.array(render.directional_light)
    intensity = al.dot(normal, -dirLight)

    if intensity > 0.9:
        
            
        b*= (texColor[0]+20)/ 255
        if b>255:
            b=255
        b*=1
        g*= 0.5
        r*= 1
        m=b
        b=r
        r=m
    elif intensity > 0.7:
                    
        b*= (texColor[0]+20)/ 255
        if b>255:
            b=255
        b*=0.8
        g*= 0.6
        r*= 0.6
        m=b
        b=r
        r=m
    elif intensity > 0.6:
                
        b*= 0.7
        g*= 0.5
        r*= 0.5
        m=b
        b=r
        r=m
        
    elif intensity > 0.4:
        r*= (texColor[2]+50)/ 255
        if r>255:
            r=255
        
        g*= 0.04
        b*= 0.04
        r*=0.6
        m=b
        b=r
        r=m
    else:
        r*= (texColor[2]+100)/ 255
        if r>255:
            r=255
        b=r
        g*= 0.3
        b*= 0.3
        r*=0.5
        m=b
        b=r
        r=m



    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0
def trunnd(n,d):
    dp = repr(n).find('.') #dot position
    if dp == -1:  
        return int(n) 
    return float(repr(n)[:dp+d+1])
def ranrgb(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= (texColor[0])/ 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = np.array(render.directional_light)
    intensity = al.dot(normal, -dirLight)
    m= random.randint(0,2)
    if m==0:
        r= 1*intensity
        if(r>1):
            r=1
        g= 0
        b=0
    if m==1:
        r= 0
        g= 1*intensity
        if(g>1):
            g=1
        b=0
        
    if m==2:
        r= 0
        g= 0
        b=1*intensity
        if(b>1):
            b=1
    if intensity > 0:

        return r, g, b
    else:
        return 0,0,0
def thermal(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= (texColor[0])/ 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = np.array(render.directional_light)
    intensity = al.dot(normal, -dirLight)
    
    if intensity>0.8:
        r= 1*intensity
        if(r>1):
            r=1
        g= 0
        b=0
    elif intensity>=0.6:
        r= 0
        g= 1*intensity
        if g>1:
            g=1
        b=0
        
    else :
        r= 0
        g= 0
        b=1*intensity
        if b>1:
            b=1
    if intensity > 0:

        return r, g, b
    else:
        return 0,0,0
def lava(render, **kwargs):
    #rend.directional_light = V3(0,-1,-1)
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= (texColor[0])/ 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = np.array(render.directional_light)
    intensity = al.dot(normal, -dirLight)
    
    m= random.randint(0,2)
    if m==0:
        r= 1*intensity
        g= 0
        b=0
        if(r>1):
            r=1
    elif m==1:
        r = 0
        g= 0
        b=0

    elif m==2:
        r= 0
        g= 0
        b=0.0

            
    if intensity > 0:
        
        return r, g, b
    else:
        return 0,0,0

def textureBlend(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    dirLight = np.array(render.directional_light)
    intensity = al.dot(normal, -dirLight)

    if intensity < 0:
        intensity = 0

    b*= intensity
    g*= intensity
    r*= intensity

    if render.active_texture2:
        texColor = render.active_texture2.getColor(tx, ty)
        b += (texColor[0] / 255) * (1 - intensity)
        g += (texColor[1] / 255) * (1 - intensity)
        r += (texColor[2] / 255) * (1 - intensity)


    return r, g, b


def normalMap(render, **kwargs):
    A, B, C = kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b/= 255
    g/= 255
    r/= 255

    if render.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w
    normal = (nX, nY, nZ)

    dirLight = np.array(render.directional_light)
    

    if render.normal_map:
        texNormal = render.normal_map.getColor(tx, ty)
        texNormal = [(texNormal[2] / 255) * 2 - 1,
                     (texNormal[1] / 255) * 2 - 1,
                     (texNormal[0] / 255) * 2 - 1]

        texNormal = texNormal / al.norm(texNormal)

        edge1 = al.subtract(B, A)
        edge2 = al.subtract(C, A)
        deltaUV1 = al.subtract(tB, tA)
        deltaUV2 = al.subtract(tC, tA)

        f = 1 / (deltaUV1[0] * deltaUV2[1] - deltaUV2[0] * deltaUV1[1])

        tangent = [f * (deltaUV2[1] * edge1[0] - deltaUV1[1] * edge2[0]),
                   f * (deltaUV2[1] * edge1[1] - deltaUV1[1] * edge2[1]),
                   f * (deltaUV2[1] * edge1[2] - deltaUV1[1] * edge2[2])]
        tangent = tangent / al.norm(tangent)
        tangent = al.subtract(tangent, al.mul(al.dot(tangent, normal), normal))
        tangent = tangent / al.norm(tangent)

        bitangent = al.cross(normal, tangent)
        bitangent = bitangent / al.norm(bitangent)

        tangentMatrix = np.matrix([[tangent[0],  bitangent[0],  normal[0]],
                                   [tangent[1],  bitangent[1],  normal[1]],
                                   [tangent[2],  bitangent[2],  normal[2]]])

        texNormal = tangentMatrix @ texNormal
        texNormal = texNormal.tolist()[0]
        texNormal = texNormal / al.norm(texNormal)
        intensity = al.dot(texNormal, -dirLight)
    else:
        intensity = al.dot(normal, -dirLight)

    b*= intensity
    g*= intensity
    r*= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0



