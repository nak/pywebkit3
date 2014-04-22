import math
import logging
import re
from pyggi.javascript import jquery
from .common import *
#Log = logging.info
context = None
tdl = None
fast = None
_ = None

import math    
# globals
gl = None                   # the gl context.
fast = None                 # the fast math lib.

Globals.g_fpsTimer = None           # object to measure frames per second
Globals.setPretty = True
Globals.checkResTimer = 2
Globals.clock = 0.0
Globals.then = 0.0
Globals.frameCount = 0
Globals.eyeClock = 0
Globals.canvas = None               # the canvas

g_logGLCalls = True   # whether or not to log webgl calls
g_debug = False      # whether or not to debug.
g_drawOnce = False
g_setSettingElements = []
g_numSettingElements = make_object({})
g_sharkWorldMats = []
g_beamWorldMats = []
g_scenes = make_object({})  # each of the models
g_sceneGroups = make_object({})  # the placement of the models
g_fog = True
g_requestId = None

#g_debug = True
#g_drawOnce = True

g_numSharks        = 0
g_tailOffsetMult   = 1
g_endOfDome        = math.pi / 8
g_tankRadius       = 74
g_tankHeight       = 36
g_standHeight      = 25
g_sharkSpeed       = 0.3
g_sharkClockOffset = 17
g_sharkXClock      = 1
g_sharkYClock      = 0.17
g_sharkZClock      = 1
g_numBubbleSets    = 10
g_laserEta = 1.2
g_laserLenFudge = 1
g_bubbleSets = []
g_fishData = []
g_numLightRays = 5
g_lightRayY = 50
g_lightRayDurationMin = 1
g_lightRayDurationRange = 1
g_lightRaySpeed = 4
g_lightRaySpread = 7
g_lightRayPosRange = 20
g_lightRayRotRange = 1.0
g_lightRayRotLerp = 0.2
g_lightRayOffset = math.pi * 2 / g_numLightRays
g_lightRayInfo = []

    
g_ui2 = [
  { 'obj': 'globals',    'name': 'speed',           'value': 1,     'max':  4 },
  { 'obj': 'globals',    'name': 'targetHeight',    'value': 0,     'max':  150 },
  { 'obj': 'globals',    'name': 'targetRadius',    'value': 88,    'max':  200 },
  { 'obj': 'globals',    'name': 'eyeHeight',       'value': 19,    'max':  150 },
  { 'obj': 'globals',    'name': 'eyeRadius',       'value': 60,    'max':  200 },
  { 'obj': 'globals',    'name': 'eyeSpeed',        'value': 0.06,  'max':  1 },
  { 'obj': 'globals',    'name': 'fieldOfView',     'value': 85,  'max':  179, 'min': 1},
  { 'obj': 'globals',    'name': 'ambientRed',      'value': 0.22,  'max':  1},
  { 'obj': 'globals',    'name': 'ambientGreen',    'value': 0.25,  'max':  1},
  { 'obj': 'globals',    'name': 'ambientBlue',     'value': 0.39,  'max':  1},
  { 'obj': 'globals',    'name': 'fogPower',        'value': 14.5,  'max':  50},
  { 'obj': 'globals',    'name': 'fogMult',         'value': 1.66,  'max':  10},
  { 'obj': 'globals',    'name': 'fogOffset',       'value': 0.53,  'max':  3},
  { 'obj': 'globals',    'name': 'fogRed',          'value': 0.54,  'max':  1},
  { 'obj': 'globals',    'name': 'fogGreen',        'value': 0.86,  'max':  1},
  { 'obj': 'globals',    'name': 'fogBlue',         'value': 1.0,   'max':  1},
  { 'obj': 'fish',       'name': 'fishHeightRange', 'value': 1,     'max':  3},
  { 'obj': 'fish',       'name': 'fishHeight',      'value': 25,    'max':  50},
  { 'obj': 'fish',       'name': 'fishSpeed',       'value': 0.124, 'max':  2},
  { 'obj': 'fish',       'name': 'fishOffset',      'value': 0.52,  'max':  2},
  { 'obj': 'fish',       'name': 'fishXClock',      'value': 1,     'max':  2},
  { 'obj': 'fish',       'name': 'fishYClock',      'value': 0.556, 'max':  2},
  { 'obj': 'fish',       'name': 'fishZClock',      'value': 1,     'max':  2},
  { 'obj': 'fish',       'name': 'fishTailSpeed',   'value': 1,     'max':  30},
  { 'obj': 'innerConst', 'name': 'refractionFudge', 'value': 3,     'max':  50},
  { 'obj': 'innerConst', 'name': 'eta',             'value': 1,     'max':  1.2},
  { 'obj': 'innerConst', 'name': 'tankColorFudge',  'value': 0.8,   'max':  2}
]
Globals.g_ui = make_objects(g_ui2)

g_netUI = [
  { 'obj': 'net',    'name': 'timeout',     'value': 3000,  'max':  3000},
  { 'obj': 'net',    'name': 'fovMult',     'value': 1.21,  'max':  2},
  { 'obj': 'net',    'name': 'fovFudge',    'value': 1,     'max':  2},
  { 'obj': 'net',    'name': 'offsetMult',  'value': 1,     'max':  2}
]
g_netUI = make_objects(g_netUI)

g_fishTable = [
  {
    'name': 'SmallFishA',
    'num': [0, 3, 36, 76, 206, 500-40-40-2-2, 1000-80-80-2-2, 2000-80-80-2-2, 4000-80-80-2-2, 50],
    'speed': 1,
    'speedRange': 1.5,
    'radius': 30,
    'radiusRange': 25,
    'tailSpeed': 10,
    'heightOffset': 0,
    'heightRange': 16,
    'constUniforms': {
    'fishLength': 10,
    'fishWaveLength': 1,
    'fishBendAmount': 2
    }
  },
  {
    'name': 'MediumFishA',
    'num': [0, 3, 6, 10, 20, 40, 80, 80, 80, 10],
    'speed': 1,
    'speedRange': 2,
    'radius': 10,
    'radiusRange': 20,
    'tailSpeed': 1,
    'heightOffset': 0,
    'heightRange': 16,
    'constUniforms': {
            'fishLength': 10,
            'fishWaveLength': -2,
            'fishBendAmount': 2
    }
  },
  {
    'name': 'MediumFishB',
    'num': [0, 2, 6, 10, 20, 40, 80, 80, 80, 10],
    'speed': 0.5,
    'speedRange': 4,
    'radius': 10,
    'radiusRange': 20,
    'tailSpeed': 3,
    'heightOffset': -8,
    'heightRange': 5,
    'constUniforms': {
      'fishLength': 10,
      'fishWaveLength': -2,
      'fishBendAmount': 2
    }
  },
  {
    'name': 'BigFishA',
    'num': [1, 1, 1, 2, 2, 2, 2, 2, 2, 3],
    'speed': 0.5,
    'speedRange': 0.5,
    'radius': 50,
    'radiusRange': 3,
    'tailSpeed': 1.5,
    'heightOffset': 0,
    'heightRange': 16,
    'lasers': True,
    'laserRot': 0.04,
    'laserOff': [0, 0.1, 9],
    'laserScale': [0.3, 0.3, 1000],
    'constUniforms': {
      'fishLength': 10,
      'fishWaveLength': -1,
      'fishBendAmount': 0.5
    }
  },
  {
    'name': 'BigFishB',
    'num': [0, 1, 1, 2, 2, 2, 2, 2, 2, 1],
    'speed': 0.5,
    'speedRange': 0.5,
    'radius': 45,
    'radiusRange': 3,
    'tailSpeed': 1,
    'heightOffset': 0,
    'heightRange': 16,
    'lasers': True,
    'laserRot': 0.04,
    'laserOff': [0, -0.3, 9],
    'laserScale': [0.3, 0.3, 1000],
    'constUniforms': {
      'fishLength': 10,
      'fishWaveLength': -0.7,
      'fishBendAmount': 0.3
    }
  },
]
g_fishTable = make_objects( g_fishTable )

g_sceneInfoByName = {
}


g_sceneInfo = [
  {
    'name': "SmallFishA",
    'program': [
      "fishVertexShader",
      "fishReflectionFragmentShader"
    ]
  },
  {
    'name': "MediumFishA",
    'program': [
      "fishVertexShader",
      "fishNormalMapFragmentShader"
    ]
  },
  {
    'name': "MediumFishB",
    'program': [
      "fishVertexShader",
      "fishReflectionFragmentShader"
    ]
  },
  {
    'name': "BigFishA",
    'program': [
      "fishVertexShader",
      "fishNormalMapFragmentShader"
    ]
  },
  {
    'name': "BigFishB",
    'program': [
      "fishVertexShader",
      "fishNormalMapFragmentShader"
    ]
  },
  {
    'name': "Arch"
  },
  {
    'name': "Coral"
  },
  {
    'name': "CoralStoneA"
  },
  {
    'name': "CoralStoneB"
  },
  {
    'name': "EnvironmentBox",
    'fog': False,
    'group': "outside",
    'program': [
      "diffuseVertexShader",
      "diffuseFragmentShader"
    ]
  },
  {
    'name': "FloorBase_Baked"
  },
  {
    'name': "FloorCenter"
  },
  {
    'name': "GlobeBase",
    'fog': False,
    'program': [
      "diffuseVertexShader",
      "diffuseFragmentShader"
    ]
  },
  {
    'name': "GlobeInner",
    'group': "inner",
    'program': [
      "innerRefractionMapVertexShader",
      "innerRefractionMapFragmentShader"
    ]
  },
  {
    'name': "GlobeOuter",
    'group': "outer",
    'blend': True,
    'program': [
      "outerRefractionMapVertexShader",
      "outerRefractionMapFragmentShader"
    ]
  },
  {
    'name': "RockA"
  },
  {
    'name': "RockB"
  },
  {
    'name': "RockC"
  },
  {
    'name': "RuinColumn"
  },
  {
    'name': "Skybox",
    'fog': False,
    'group': "outside",
    'program': [
      "diffuseVertexShader",
      "diffuseFragmentShader"
    ]
  },
  {
    'name': "Stone"
  },
  {
    'name': "Stones"
  },
  {
    'name': "SunknShip"
  },
  {
    'name': "SunknSub"
  },
  {
    'name': "SupportBeams",
    'group': "outside",
    'fog': False
  },
  {
    'name': "SeaweedA",
    'blend': True,
    'group': "seaweed",
    'program': [
      "seaweedVertexShader",
      "seaweedFragmentShader",
    ]
  },
  {
    'name': "SeaweedB",
    'blend': True,
    'group': "seaweed",
    'program': [
      "seaweedVertexShader",
      "seaweedFragmentShader",
    ]
  },
  {
    'name': "TreasureChest"
  }
]
g_sceneInfo = make_objects( g_sceneInfo )

g_skyBoxUrls = [
  'assets/GlobeOuter_EM_positive_x.jpg',
  'assets/GlobeOuter_EM_negative_x.jpg',
  'assets/GlobeOuter_EM_positive_y.jpg',
  'assets/GlobeOuter_EM_negative_y.jpg',
  'assets/GlobeOuter_EM_positive_z.jpg',
  'assets/GlobeOuter_EM_negative_z.jpg'
#  'static_assets/skybox/InteriorCubeEnv_EM.png'
]

def ValidateNoneOfTheArgsAreUndefined(functionName, args):
    for  ii in range(len(args)):
        if (args[ii] == None):
            tdl.error("undefined passed to gl." + functionName + "(" +
                      tdl.webgl.glFunctionArgsToString(functionName, args) + ")")             
  


def LogGLCall(functionName, args):
  if (g_logGLCalls):
      ValidateNoneOfTheArgsAreUndefined(functionName, args)
      tdl.log("gl." + functionName + "(" +
              tdl.webgl.glFunctionArgsToString(functionName, args) + ")")
  


#/**
# * Calculate the intersection of a ray and a sphere
# *
# * point1 + mu1 (point2 - point1)
# * point1 + mu2 (point2 - point1)
# *
# * Return undefined.
# */
def raySphereIntersection(point1, point2, center, radius):
    kEpsilon = 0.0001
    dp = [
        point2[0] - point1[0],
        point2[1] - point1[1],
        point2[2] - point1[2]]
    a = dp[0] * dp[0] + \
      dp[1] * dp[1] + \
      dp[2] * dp[2]
    b = 2 * (dp[0] * (point1[0] - center[0]) +
             dp[1] * (point1[1] - center[1]) +
             dp[2] * (point1[2] - center[2]))
    c = center[0] * center[0] + \
        center[1] * center[1] + \
        center[2] * center[2]
    c += point1[0] * point1[0] + \
         point1[1] * point1[1] + \
         point1[2] * point1[2]
    c -= 2 * (center[0] * point1[0] + \
              center[1] * point1[1] + \
              center[2] * point1[2])
    c -= radius * radius
    bb4ac = b * b - 4 * a * c
    if (abs(a) < kEpsilon or bb4ac < 0):
        return


    sq = math.sqrt(bb4ac)
    mu1 = (-b + sq) / (2 * a)
    mu2 = (-b - sq) / (2 * a)

    m = max(mu1, mu2)
    from operator import add
    return map(add, point1, [p*m for p in dp])


def refract(i, n, eta):
    from operator import mul
    dotNI = sum(map(mul, n, i))
    k = 1.0 - eta * eta * (1.0 - dotNI * dotNI)
    if (k < 0.0):
        return None
        
    return tdl.math.subVector(
      tdl.math.mulScalarVector(eta, i),
      tdl.math.mulScalarVector(eta * dotNI + math.sqrt(k), n))

def createProgramFromTags(
    vertexTagId,
    fragmentTagId,
    fog = False,
    opt_reflection = False,
    opt_normalMaps = False):

    
    opt_reflection = (opt_reflection == None) or  opt_reflection
    opt_normalMaps = (opt_normalMaps == None) or opt_normalMaps

    fogUniforms = '' + \
                  'uniform float fogPower\n' + \
                  'uniform float fogMult\n' + \
                  'uniform float fogOffset\n' + \
                  'uniform vec4 fogColor\n'
    fogCode = '' + \
              'outColor = mix(outColor, vec4(fogColor.rgb, diffuseColor.a),\n' + \
              '   clamp(pow((v_position.z / v_position.w), fogPower) * fogMult - fogOffset,0.0,1.0))\n'
    fs = getScriptText(fragmentTagId)

    if (g_fog and fog):
        fs = re.sub('# #fogUniforms', fogUniforms,fs)
        fs = re.sub('# #fogCode', fogCode,fs)

    if (opt_reflection) :
        fs = re.sub("/^.*?\/\/ #noReflection\n/gm", "",str(fs))
    else:
        fs = re.sub("/^.*?\/\/ #reflection\n/gm", "",str(fs))


    if (opt_normalMaps):
        fs = re.sub("/^.*?\/\/ #noNormalMap\n/gm", "",fs)
    else:
        fs = re.sub("/^.*?\/\/ #normalMap\n/gm", "",fs)


    return tdl.programs.loadProgram(getScriptText(vertexTagId), fs)

from pyggi.javascript import JavascriptClass
    
class Scene(object):

  def __init__(self,opt_programIds, fog):
      global context
      #JavascriptClass.__init__(self, context, "scene")
      self.programIds = opt_programIds
      self.bad = False
      self.loaded = False
      self.fog = fog
      self.models = []
      self.ignore = False


  def load(self, url):
      that = self
      self.url = url
      tdl.io.loadJSON(url, self.onload_)     

  def stop(self):
      self.ignore = False

  def onload_(self, data, exception, *argsz):
      if (self.ignore):
          return
  
      self.loaded = True
      if (exception):
          self.bad = True
      for mm in range( len(data.models) ):
          model = data.models[mm]
          # setup textures
          textures = {}
          for  name in model.textures:
              textures[name] = tdl.textures.loadTexture(
                  'assets/' + model.textures[name], True)
      
      # setup vertices
      arrays = {}
      for  name in model.fields:
          field = model.fields[name]
          arrays[name] = tdl.primitives.AttribBuffer(
              field.numComponents,
              field.data,
              field.type)
      
      # setup program
      # There are 3 programs
      # DM
      # DM+NM
      # DM+N
      # M+RM
      atype = None
      vsId = None
      fsId = None
      if (not textures.diffuse):
          raise Exception( "missing diffuse texture for: " + self.url )
      
      if (self.programIds):
        atype = "custom"
        vsId = self.programIds[0]
        fsId = self.programIds[1]
        # Fix self hack
        textures.skybox = tdl.textures.loadTexture(g_skyBoxUrls)
      elif (textures.reflectionMap):
        if (not textures.normalMap):
          raise Exception( "missing normalMap for: " + self.url )
        
        atype = "reflection"
        vsId = 'reflectionMapVertexShader'
        fsId = 'reflectionMapFragmentShader'
        textures.skybox = tdl.textures.loadTexture(g_skyBoxUrls)

      elif (textures.normalMap):
        atype = "normalMap"
        vsId = 'normalMapVertexShader'
        fsId = 'normalMapFragmentShader'
      else:
        atype = "diffuse"
        vsId = 'diffuseVertexShader'
        fsId = 'diffuseFragmentShader'
      
      program = createProgramFromTags(vsId, fsId, self.fog)
      noFog = createProgramFromTags(vsId, fsId, False)
      noReflection = createProgramFromTags(vsId, fsId, self.fog, False)
      noFognoReflection = createProgramFromTags(vsId, fsId, False, False)
      noNormalMaps = createProgramFromTags(vsId, fsId, self.fog, False)
      noFognoNormalMaps =\
          createProgramFromTags(vsId, fsId, False, False)
      noReflectionnoNormalMaps =\
          createProgramFromTags(vsId, fsId, self.fog, False, False)
      noFognoReflectionnoNormalMaps =\
          createProgramFromTags(vsId, fsId, False, False, False)

      tdl.log(self.url, ": ", atype)
      model = tdl.models.Model(program, arrays, textures)
      model.programs = {
        base: program,
        noFog: noFog,
        noReflection: noReflection,
        noFognoReflection: noFognoReflection,
        noNormalMaps: noNormalMaps,
        noFognoNormalMaps: noFognoNormalMaps,
        noReflectionnoNormalMaps: noReflectionnoNormalMaps,
        noFognoReflectionnoNormalMaps: noFognoReflectionnoNormalMaps
      }
      model.extents = arrays['position'].computeExtents()
      self.models.push(model)
    
      setShaders()
  

def setShaders():
    name = ''
    if (not Globals.g.options.fog.enabled):
        name += 'noFog'
  
    if (not Globals.g.options.reflection.enabled):
        name += 'noReflection'
  
    if (not Globals.g.options.normalMaps.enabled):
        name += 'noNormalMaps'
  
    if (name == ''):
        name = 'base'
  
    for sceneName in g_scenes:
        scene = g_scenes[sceneName]
        models = scene.models
        numModels = len(models)
        for jj in range( numModels):
            model = models[jj]
            model.setProgram(model.programs[name])





def loadScene(name, opt_programIds, fog):
    logging.error("LOADING SCENE ... '%s' \n'%s' \n'%s'", name, opt_programIds, fog)
    scene = Scene(opt_programIds, fog)
    scene.load("assets/" + name + ".js")
    return scene


def loadScenes():
    logging.error("LOADING SCENES")
    logging.error("---------> %s"%len(g_sceneInfo))
    for ii in range( len(g_sceneInfo) ):
        info = g_sceneInfo[ii]
        fog = True
        if 'fog' not in info:
            fog = info.fog
        try:
            logging.error("LOADING SCENE %s %s %s"%(info.name, info.program, fog))
            sc  = loadScene(info.name, info.program, fog)
            logging.error("ASSIGNING SCENE ...")
            g_scenes[info.name] = sc
        except:
            import traceback
            traceback.print_exc()
            raise

def loadPlacement():
    def loadit( json, exception):
        if (exception):
          raise Exception( exception )
        else:
          for ii in range(len(g_sceneInfo)):
              info = g_sceneInfo[ii]
              g_sceneInfoByName[info.name] = info
          

          objects = json.objects
          for  ii in range(objects.length):
              object = objects[ii]
              scene = g_scenes[object.name]
              info = g_sceneInfoByName[object.name]
              #tdl.log(object.name)
              groupName = info.group or 'base'
              if (not g_sceneGroups[groupName]):
                  g_sceneGroups[groupName] = []
            
              group = g_sceneGroups[groupName]
              group.push(object)
          
        
        
    tdl.io.loadJSON('assets/PropPlacement.js', loadit)

import random

def initLightRay(info):
    info['duration'] =\
          g_lightRayDurationMin + random.gauss(0.5,0.5) * \
          g_lightRayDurationRange
    info['timer'] = info['duration']
    r = random.gauss(0.5,0.5)
    info['rot'] = r * g_lightRayRotRange
    info['x'] = (r - 0.5) * g_lightRayPosRange

#/**
# * Setup Laser
# */
def setupLaser():
    textures = {
        'colorMap': tdl.textures.loadTexture('static_assets/beam.png')}
    program = createProgramFromTags(
                    'laserVertexShader',
        'laserFragmentShader')
    beam1Arrays = tdl.primitives.createPlane(1, 1, 1, 1)
    #del beam1Arrays.normal
    tdl.primitives.reorient(beam1Arrays,
                            tdl.math.matrix4.translation([0, 0, 0.5]))
    beam2Arrays = tdl.primitives.clone(beam1Arrays)
    beam3Arrays = tdl.primitives.clone(beam1Arrays)
    tdl.primitives.reorient(beam2Arrays,
                        tdl.math.matrix4.rotationZ(tdl.math.degToRad(120)))
    tdl.primitives.reorient(beam3Arrays,
                        tdl.math.matrix4.rotationZ(tdl.math.degToRad(-120)))
    arrays = tdl.primitives.concat([
        beam1Arrays,
        beam2Arrays,
        beam3Arrays])
    return tdl.models.Model(program, arrays, textures)


def setupLightRay():
  for  ii in range( g_numLightRays):
      info = { }
      l = ii / g_numLightRays
      initLightRay(info)
      g_lightRayInfo.append( make_object(info) )
  

  textures = {
      'colorMap': tdl.textures.loadTexture('assets/LightRay.png') }
  program = createProgramFromTags(
      'texVertexShader',
      'texFragmentShader')
  arrays = tdl.primitives.createPlane(1, 1, 1, 1)
  tdl.primitives.reorient(arrays,
      [1, 0, 0, 0,
       0, 0, -1, 0,
       0, 1, 0, 0,
       0, 0.5, 0, 1])
  #del arrays.normal
  logging.error("LASER %s %s %s"%(program, arrays, textures))
  ret =  tdl.models.Model(program, arrays, textures)
  logging.error("LASER RET")
  return ret


def setupBubbles(particleSystem):
    texture = tdl.textures.loadTexture('static_assets/bubble.png')
    logging.error("SETUP BUBBLES %s"%particleSystem)
    emitter = particleSystem.createParticleEmitter(texture.texture)
    emitter.setTranslation(0, 0, 0)
    emitter.setState(tdl.particles.ParticleStateIds.ADD)
    emitter.setColorRamp(
        [1, 1, 1, 1,
         1, 1, 1, 1,
         1, 1, 1, 1,
         1, 1, 1, 1,
         1, 1, 1, 1,
         1, 1, 1, 0])
    emitter.setParameters({
        'numParticles': 100,
        'numFrames': 1,
        'frameDuration': 1000.0,
        'frameStartRange': 0,
        'lifeTime': 40,
        'startTime': 0,
        'startSize': 0.01,
        'startSizeRange': 0.01,
        'endSize': 0.4,
        'endSizeRange': 0.2,
        'position': [0,-2,0],
        'positionRange': [0.1,2,0.1],
        'acceleration': [0,0.05,0],
        'accelerationRange': [0,0.02,0],
        'velocityRange': [0.05,0,0.05],
        'colorMult': [0.7,0.8,1,1]})
        #function(index, parameters) {
        #    var speed = Math.random() * 0.6 + 0.2
        #    var speed2 = Math.random() * 0.2 + 0.1
        #    var angle = Math.random() * 2 * math.pi
        #    parameters.velocity = math.matrix4.transformPoint(
        #        math.matrix4.rotationZ(angle), [speed, speed2, 0])
        #}
        #)
    for ii in range( g_numBubbleSets):
        g_bubbleSets[ii] = emitter.createOneShot()
    logging.error("SETUP BUBBLES 2")
    


#/**
# * Sets up the Skybox
# */
def setupSkybox():
  textures = {
    'skybox': tdl.textures.loadTexture(g_skyBoxUrls)}
  program = createProgramFromTags(
      'skyboxVertexShader',
      'skyboxFragmentShader')
  logging.error("############# SKYBOX 1 %s"%tdl.primitives.createPlane)
  arrays = tdl.primitives.createPlane(2, 2, 1, 1)
  #del arrays['normal']
  #del arrays['texCoord']
  logging.error("############# SKYBOX 2")
  tdl.primitives.reorient(arrays,
      [1, 0, 0, 0,
       0, 0, 1, 0,
       0,-1, 0, 0,
       0, 0, 0.99, 1])
  logging.error("############# SKYBOX")
  return tdl.models.Model(program, arrays, textures)


def setViewSettings(index):
  def setGlobal(name, value):
        _(g_uiWidgets.globals[name]).slider("value", value * 1000)
        Globals.g.globals[name] = value
  

  viewSettings = g_viewSettings[index]
  setSettings({globals: viewSettings})


def advanceViewSettings():
  setViewSettings(g_viewSettingsIndex)
  g_viewSettingsIndex = (g_viewSettingsIndex + 1) % g_viewSettings.length


#/**
# * Sets the count
# */
def setSetting(elem, id):
    if id == 10:
        pass
    elif id == 9:
        advanceViewSettings()
    else:
        g_numSettingElements[id] = elem
        setSettings({globals:{fishSetting:id}})
        for  otherElem in g_numSettingElements:
            g_numSettingElements[otherElem].style.color = "gray"
    
    elem.style.color = "red"
  


#/**
# * Initializes stuff.
# */
def main( document ):
  global gl

  Globals.canvas = document.getElementById("canvas")

  #clanvas = WebGLDebugUtils.makeLostContextSimulatingCanvas(canvas)
  # tell the simulator when to lose context.
  #canvas.loseContextInNCalls(1500)

  tdl.webgl.registerContextLostHandler(Globals.canvas, handleContextLost)
  tdl.webgl.registerContextRestoredHandler(Globals.canvas, handleContextRestored)
  tdl.fps.FPSTimer.promote_to_constructor()
  Globals.g_fpsTimer =  tdl.fps.FPSTimer()
  logging.error("GFPS IS %s"%Globals.g_fpsTimer)
  assert(Globals.g_fpsTimer is not None)
  gl = tdl.webgl.setupWebGL(Globals.canvas, Globals.g.globals.canvasAttributes)
  if (not gl):
      return False
  
  if (g_debug):
      gl = tdl.webgl.makeDebugContext(gl, None, LogGLCall)
  

  initialize()


def handleContextLost():
  tdl.log("context lost")
  tdl.webgl.cancelRequestAnimationFrame(g_requestId)
  # remove loading scenes
  for name in g_scenes:
      scene = g_scenes[name]
      scene.stop()
  
  g_scenes = { }


def handleContextRestored():
    tdl.log("context restored")
    initialize()

import array
def Float32Array(l):
    if isinstance(l, list):
        return array.array('f', l)
    else:
        return array.array('f', [0.0 for _ in range(l)])


def tryit():
    raise Exception("TRIED")

def initialize():
    window = context.get_jsobject("window")
    window.setTimeout( tryit, 100)
    
    maxViewportDims = gl.getParameter(gl.MAX_VIEWPORT_DIMS)
    
    gl.enable(gl.DEPTH_TEST)
    gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA)
    
    loadPlacement()
    Log("--Setup Skybox---------------------------------------")
    skybox = setupSkybox()
    Log("--Load Scenes---------------")
    loadScenes()
    Log("--Setup Laser----------------------------------------")
    document =  context.get_jsobject("document")
    laser = setupLaser()
    Log("--Populating fish data------")
    for  ff in  g_fishTable:
        ff.fishData = []
  
    particleSystem = tdl.particles.ParticleSystem(
        gl, None, random.gauss(0.5,0.5))
    Log("--Populated ----")
    if particleSystem:
        setupBubbles(particleSystem)
    bubbleTimer = 0
    bubbleIndex = 0

    lightRay = setupLightRay()
    Log("--Setup light rays--- %s"%document)
    Globals.then = 0.0
    fpsElem = document.getElementById("fps")

    import logging
    logging.error("Populating float array")
    projection = Float32Array(16)
    view = Float32Array(16)
    world = Float32Array(16)
    worldInverse = Float32Array(16)
    worldInverseTranspose = Float32Array(16)
    viewProjection = Float32Array(16)
    worldViewProjection = Float32Array(16)
    viewInverse = Float32Array(16)
    viewProjectionInverse = Float32Array(16)
    skyView = Float32Array(16)
    skyViewProjection = Float32Array(16)
    skyViewProjectionInverse = Float32Array(16)
    eyePosition = Float32Array(3)
    target = Float32Array(3)
    up = Float32Array([0,1,0])
    lightWorldPos = Float32Array(3)
    v3t0 = Float32Array(3)
    v3t1 = Float32Array(3)
    m4t0 = Float32Array(16)
    m4t1 = Float32Array(16)
    m4t2 = Float32Array(16)
    m4t3 = Float32Array(16)
    zero4 = Float32Array(4)
    one4 = Float32Array([1,1,1,1])
    colorMult = Float32Array([1,1,1,1])
    ambient = Float32Array(4)
    fogColor = Float32Array([1,1,1,1])
    
    # Sky uniforms.
    skyConst = make_object({'viewProjectionInverse': skyViewProjectionInverse})
    skyPer = make_object({})

    # Sand uniforms.
    sandConst = make_object({
        'viewInverse': viewInverse,
        'lightWorldPos': lightWorldPos,
        'lightColor': one4,
        'specular': one4,
        'shininess': 5,
        'specularFactor': 0.3})
    sandPer = make_object({
        'world': world,
        'worldViewProjection': worldViewProjection,
        'worldInverse': worldInverse,
        'worldInverseTranspose': worldInverseTranspose})
    
    # Generic uniforms.
    genericConst = make_object({
        'viewInverse': viewInverse,
        'lightWorldPos': lightWorldPos,
        'lightColor': one4,
        'specular': one4,
        'shininess': 50,
        'specularFactor': 1,
        'ambient': ambient})
    genericPer = make_object({
        'world': world,
        'worldViewProjection': worldViewProjection,
        'worldInverse': worldInverse,
        'worldInverseTranspose': worldInverseTranspose})
    
    # outside uniforms.
    outsideConst = make_object({
        'viewInverse': viewInverse,
        'lightWorldPos': lightWorldPos,
        'lightColor': one4,
        'specular': one4,
        'shininess': 50,
        'specularFactor': 0,
        'ambient': ambient})
    outsidePer = make_object({
        'world': world,
        'worldViewProjection': worldViewProjection,
        'worldInverse': worldInverse,
        'worldInverseTranspose': worldInverseTranspose})
    
    # Seaweed uniforms.
    seaweedConst = make_object({
        'viewInverse': viewInverse,
        'lightWorldPos': lightWorldPos,
        'lightColor': one4,
        'specular': one4,
        'shininess': 50,
        'specularFactor': 1,
        'ambient': ambient})
    seaweedPer = make_object({
        'world': world,
        'viewProjection': viewProjection,
        'worltdInverse': worldInverse,
        'worldInverseTranspose': worldInverseTranspose})
    
    # Laser uniforms
    laserConst = make_object({})
    laserPer = make_object({
        'worldViewProjection': worldViewProjection})

    # Inner uniforms.
    Globals.g.innerConst.viewInverse = viewInverse
    Globals.g.innerConst.lightWorldPos = lightWorldPos
    Globals.g.innerConst.lightColor = one4
    Globals.g.innerConst.specular = one4
    Globals.g.innerConst.shininess = 50
    Globals.g.innerConst.specularFactor = 1
    innerPer = make_object({
        'world': world,
        'worldViewProjection': worldViewProjection,
        'worldInverse': worldInverse,
        'worldInverseTranspose': worldInverseTranspose})
    
    # Fish uniforms.
    fishConst = make_object({
        'viewProjection': viewProjection,
        'viewInverse': viewInverse,
        'lightWorldPos': lightWorldPos,
        'lightColor': one4,
        'specular': one4,
        'shininess': 5,
        'specularFactor': 0.3,
        'ambient': ambient})
    fishPer = make_object({
        'worldPosition': Float32Array(3), #[0,0,0],
        'nextPosition': Float32Array(3), #[0,0,0],
        'scale': 1})
    
    # lightRay uniforms.
    lightRayConst = make_object({})
    lightRayPer = make_object({
        'worldViewProjection': worldViewProjection,
        'colorMult': Float32Array([1,1,1,1])})
    theClock = tdl.clock.createClock({True:10, False:None}[Globals.g.net.sync or False])
    def DrawGroup(group, constUniforms, perUniforms):
        numObjects = group.length
        currentModel = None
        for ii in range(numObjs):
            obj = group[ii]
            scene = g_scenes[obj.name]
            info = g_sceneInfoByName[obj.name]
            if (not scene):
                g_scenes[obj.name] = { missing: True }
                tdl.log("missing scene:", obj.name)
                continue

            if (scene.missing or not scene.loaded):
                continue


            if (info.blend):
                gl.enable(gl.BLEND)
            else:
                gl.disable(gl.BLEND)


            models = scene.models
            numModels = models.length
            for  jj in range(numModels):
                 model = models[jj]
                 if (model != currentModel):
                     currentModel = model
                     model.drawPrep(constUniforms)

            fast.matrix4.copy(world, obj.worldMatrix)
            fast.matrix4.mul(worldViewProjection, world, viewProjection)
            fast.matrix4.inverse(worldInverse, world)
            fast.matrix4.transpose(worldInverseTranspose, worldInverse)
            perUniforms.time = Globals.clock + ii
            model.draw(perUniforms)




        initUIStuff()
        initializeCommon()


        now = theClock.getTime()
        if (Globals.g.net.sync):
            Globals.clock = now
            Globals.eyeClock = now


    def setCanvasSize(canvas, newWidth, newHeight):
        changed = False
        ratio = {True: window.devicePixelRatio, False:1}[Globals.g.win.useDevicePixelRation and window.devicePixelRatio]
        newWidth *= ratio
        newHeight *= ratio
        if (newWidth != canvas.width):
            canvas.width = newWidth
            changed = True
            tdl.log("canvas width:", newWidth)

        if (newHeight != canvas.height):
            canvas.height = newHeight
            changed = True
            tdl.log("canvas height:", newHeight)

        if (changed):
            #tdl.log("drawingBufferDimensions:" + gl.drawingBufferWidth + ", " + gl.drawingBufferHeight)
            gl.viewport(0, 0, gl.drawingBufferWidth, gl.drawingBufferHeight)

        return changed


    def increaseCanvasSize(canvas):
        #tdl.log(canvas.width, canvas.clientWidth, canvas.width / canvas.clientWidth)
        #tdl.log(canvas.height, canvas.clientHeight, canvas.height / canvas.clientHeight)
        newWidth = min(maxViewportDims[0],
                       canvas.width * ({True:2, False:1}[canvas.clientWidth / canvas.width > 1.2]))
        newHeight = min(maxViewportDims[1],
                        canvas.height * ({True:2, False:1}[(canvas.clientHeight / canvas.height > 1.2)] ) )
        return setCanvasSize(canvas, newWidth, newHeight)


    def decreaseCanvasSize(canvas):
        newWidth = max(512,
                            canvas.width * ({True:0.5, False:1}[canvas.clientWidth / canvas.width]))
        newHeight = max(512,
                             canvas.height * ({True:0.5, False:1}[canvas.clientHeight / canvas.height < 0.5]))


    #??????????    
        if ('width' in Globals.g.globals and 'height' in Globals.g.globals):
            return setCanvasSize(canvas, Globals.g.globals.width, Globals.g.globals.height)
        else:
            return setCanvasSize(canvas, newWidth, newHeight)
    def render(*args):
      try:    
        
        import logging
        logging.error("RENDER")
        global g_logGLCalls
        now = theClock.getTime()
        elapsedTime = None
        if(Globals.then == 0.0):
            elapsedTime = 0.0
        else:
            elapsedTime = now - Globals.then

        Globals.then = now

        Globals.frameCount += 1

        Globals.g_fpsTimer.update(elapsedTime)
        fpsElem.innerHTML = Globals.g_fpsTimer.averageFPS

        # If we are running > 40hz then turn on a few more options.
        #if (Globals.setPretty and Globals.g_fpsTimer.averageFPS > 40):
        #    Globals.ssetPretty = False
        #    if (not Globals.g.options.normalMaps.enabled): Globals.g.options.normalMaps.toggle() 
        #    if (not Globals.g.options.reflection.enabled): Globals.g.options.reflection.toggle() 


        # See if we should increase/decrease the rendering resolution
        logging.error("CHECK TIMER")
        Globals.checkResTimer -= elapsedTime
        if (Globals.checkResTimer < 0):
            if (Globals.g.win and Globals.g.win.adjustRes):
                if (Globals.g_fpsTimer.averageFPS > 35):
                    if (increaseCanvasSize(canvas)):
                        Globals.checkResTimer = 2

                elif (Globals.g_fpsTimer.averageFPS < 15):
                    if (decreaseCanvasSize(canvas)):
                        Globals.checkResTimer = 2




        logging.error("SYNC? %s"%Globals.g.net.sync)
        if (Globals.g.net.sync):
            Globals.clock = now * Globals.g.globals.speed
            Globals.eyeClock = now * Globals.g.globals.eyeSpeed
        else:
            # we have our own clock.
            Globals.clock += elapsedTime * Globals.g.globals.speed
            Globals.eyeClock += elapsedTime * Globals.g.globals.eyeSpeed

        logging.error("UPDATE 1")
        eyePosition[0] = math.sin(Globals.eyeClock) * Globals.g.globals.eyeRadius
        eyePosition[1] = Globals.g.globals.eyeHeight
        eyePosition[2] = math.cos(Globals.eyeClock) * Globals.g.globals.eyeRadius
        target[0] = math.sin(Globals.eyeClock + math.pi) * Globals.g.globals.targetRadius
        target[1] = Globals.g.globals.targetHeight
        target[2] = math.cos(Globals.eyeClock + math.pi) * Globals.g.globals.targetRadius

        ambient[0] = Globals.g.globals.ambientRed
        ambient[1] = Globals.g.globals.ambientGreen
        ambient[2] = Globals.g.globals.ambientBlue

        logging.error("UPDATE 2")
        gl.colorMask(True, True, True, True)
        gl.clearColor(0,0.8,1,0)
        gl.clear(int(gl.COLOR_BUFFER_BIT) | int(gl.DEPTH_BUFFER_BIT) |
                 int(gl.STENCIL_BUFFER_BIT))

        near = 1
        far = 25000
        
        aspect = Globals.canvas.clientWidth / Globals.canvas.clientHeight
        top = math.tan(tdl.math.degToRad(Globals.g.globals.fieldOfView * Globals.g.net.fovFudge) * 0.5) * near
        bottom = -top
        left = aspect * bottom
        right = aspect * top
        width = abs(right - left)
        height = abs(top - bottom)
        xOff = width * Globals.g.net.offset[0] * Globals.g.net.offsetMult
        yOff = height * Globals.g.net.offset[1] * Globals.g.net.offsetMult
        logging.error("UPDATE 3")
        tdl.fast.matrix4.frustum(
          projection,
          left + xOff,
          right + xOff,
          bottom + yOff,
          top + yOff,
          near,
          far)

        tdl.fast.matrix4.cameraLookAt(
            viewInverse,
            eyePosition,
            target,
            up)
        if ('slave' in Globals.g.net and Globals.g.net.slave):
            # compute X fov from y fov
            fovy = tdl.math.degToRad(Globals.g.globals.fieldOfView * Globals.g.net.fovFudge)
            fovx = math.atan(
                math.tan(fovy * 0.5) * Globals.canvas.clientWidth / Globals.canvas.clientHeight) * 2
            fast.matrix4.rotationY(
                m4t0, Globals.g.net.rotYMult * fovx * -g.net.fovMult)
            fast.matrix4.mul(viewInverse, m4t0, viewInverse)

        tdl.fast.matrix4.inverse(view, viewInverse)
        tdl.fast.matrix4.mul(viewProjection, view, projection)
        tdl.fast.matrix4.inverse(viewProjectionInverse, viewProjection)

        tdl.fast.matrix4.copy(skyView, view)
        skyView[12] = 0
        skyView[13] = 0
        skyView[14] = 0
        tdl.fast.matrix4.mul(skyViewProjection, skyView, projection)
        tdl.fast.matrix4.inverse(skyViewProjectionInverse, skyViewProjection)

        tdl.fast.matrix4.getAxis(v3t0, viewInverse, 0) # x
        tdl.fast.matrix4.getAxis(v3t1, viewInverse, 1) # y
        tdl.fast.mulScalarVector(v3t0, 20, v3t0)
        tdl.fast.mulScalarVector(v3t1, 30, v3t1)
        tdl.fast.addVector(lightWorldPos, eyePosition, v3t0)
        tdl.fast.addVector(lightWorldPos, lightWorldPos, v3t1)

    #      view: view,
    #      projection: projection,
    #      viewProjection: viewProjection,

        gl.disable(gl.BLEND)
        gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA)
        gl.blendEquation(gl.FUNC_ADD)
        gl.enable(gl.CULL_FACE)

        tdl.math.resetPseudoRandom()
        pseudoRandom = tdl.math.pseudoRandom
        #pseudoRandom = function() {
        #  return 0.5
        #}

        # Draw Skybox
        #Log("--Draw Sky---------------------------------------")
        #if (Globals.g.options.skybox.enabled) {
        #  gl.depthMask(False)
        #  skybox.drawPrep(skyConst)
        #  skybox.draw(skyPer)
        #}
        gl.depthMask(True)

        if (g_fog):
            genericConst.fogPower  = Globals.g.globals.fogPower
            genericConst.fogMult   = Globals.g.globals.fogMult
            genericConst.fogOffset = Globals.g.globals.fogOffset
            genericConst.fogOffset = Globals.g.globals.fogOffset
            genericConst.fogColor  = fogColor
            fishConst.fogPower     = Globals.g.globals.fogPower
            fishConst.fogMult      = Globals.g.globals.fogMult
            fishConst.fogOffset    = Globals.g.globals.fogOffset
            fishConst.fogColor     = fogColor
            Globals.g.innerConst.fogPower  = Globals.g.globals.fogPower
            Globals.g.innerConst.fogMult   = Globals.g.globals.fogMult
            Globals.g.innerConst.fogOffset = Globals.g.globals.fogOffset
            Globals.g.innerConst.fogColor  = fogColor
            seaweedConst.fogPower  = Globals.g.globals.fogPower
            seaweedConst.fogMult   = Globals.g.globals.fogMult
            seaweedConst.fogOffset = Globals.g.globals.fogOffset
            seaweedConst.fogColor  = fogColor
            fogColor[0] = Globals.g.globals.fogRed
            fogColor[1] = Globals.g.globals.fogGreen
            fogColor[2] = Globals.g.globals.fogBlue


        # Draw Scene
        if (g_sceneGroups.base):
            DrawGroup(g_sceneGroups.base, genericConst, genericPer)


        # Draw Fishes.
        Log("--Draw Fish---------------------------------------")

        gl.enable(gl.BLEND)
        fast = tdl.fast
        for ff in range(len(g_fishTable)):
            
            fishInfo = g_fishTable[ff]
            fishName = fishInfo.name
            numFish = fishInfo.num[Globals.g.globals.fishSetting]
            matMul = fast.matrix4.mul
            matInverse = fast.matrix4.inverse
            matScaling = fast.matrix4.scaling
            matCameraLookAt = fast.matrix4.cameraLookAt
            matTranspose = fast.matrix4.transpose
            scene = g_scenes[fishName]
            if (scene and scene.loaded and not scene.bad):
                fish = scene.models[0]
                f = Globals.g.fish
                for  p in fishInfo.constUniforms:
                    fishConst[p] = fishInfo.constUniforms[p]

                fish.drawPrep(fishConst)
                fishBaseClock = Globals.clock * f.fishSpeed
                fishRadius = fishInfo.radius
                fishRadiusRange = fishInfo.radiusRange
                fishSpeed = fishInfo.speed
                fishSpeedRange = fishInfo.speedRange
                fishTailSpeed = fishInfo.tailSpeed * f.fishTailSpeed
                fishOffset = f.fishOffset
                fishClockSpeed = f.fishSpeed
                fishHeight = f.fishHeight + fishInfo.heightOffset
                fishHeightRange = f.fishHeightRange * fishInfo.heightRange
                fishXClock = f.fishXClock
                fishYClock = f.fishYClock
                fishZClock = f.fishZClock
                fishPosition = fishPer.worldPosition
                fishNextPosition = fishPer.nextPosition
                for ii in range(numFish):
                    fishClock = fishBaseClock + ii * fishOffset
                    speed = fishSpeed + math.pseudoRandom() * fishSpeedRange
                    scale = 1.0 + math.pseudoRandom() * 1
                    xRadius = fishRadius + pseudoRandom() * fishRadiusRange
                    yRadius = 2.0 + pseudoRandom() * fishHeightRange
                    zRadius = fishRadius + pseudoRandom() * fishRadiusRange
                    fishSpeedClock = fishClock * speed
                    xClock = fishSpeedClock * fishXClock
                    yClock = fishSpeedClock * fishYClock
                    zClock = fishSpeedClock * fishZClock

                    fishPosition[0] = math.sin(xClock) * xRadius
                    fishPosition[1] = math.sin(yClock) * yRadius + fishHeight
                    fishPosition[2] = math.cos(zClock) * zRadius
                    fishNextPosition[0] = math.sin(xClock - 0.04) * xRadius
                    fishNextPosition[1] = math.sin(yClock - 0.01) * yRadius + fishHeight
                    fishNextPosition[2] = math.cos(zClock - 0.04) * zRadius
                    fishPer.scale = scale

                    fishPer.time = \
                                 ((clock + ii * g_tailOffsetMult) * fishTailSpeed * speed) % \
                                 (math.pi * 2)
                    fish.draw(fishPer)

                    if (Globals.g.drawLasers and fishInfo.lasers):
                        fishInfo.fishData[ii] = {
                            position: [
                                fishPosition[0],
                                fishPosition[1],
                                fishPosition[2]],
                            target: [
                                fishNextPosition[0],
                                fishNextPosition[1],
                                fishNextPosition[2]],
                            scale: scale,
                            time: fishPer.time
                            }




            Log("--Drew fish-----------------------%s")
            if (Globals.g.options.tank.enabled):
                if (g_sceneGroups.inner):
                    Log("--Draw GlobeInner----------------")
                    DrawGroup(g_sceneGroups.inner, Globals.g.innerConst, innerPer)


        logging.error("SEAWEED %s"%g_sceneGroups.seaweed)
        if (g_sceneGroups.seaweed):
            Log("--Draw Seaweed----------------")
            DrawGroup(g_sceneGroups.seaweed, seaweedConst, seaweedPer)


        logging.error("LASERS %s"%Globals.g.drawLasers)
        # Draw Lasers
        if (Globals.g.drawLasers):
            Log("--Draw Lasers---------------------------------------")
            gl.enable(gl.BLEND)
            gl.blendFunc(gl.ONE, gl.ONE)
            gl.disable(gl.CULL_FACE)
            gl.depthMask(False)

            laser.drawPrep(laserConst)
            c = 0.5 + (Globals.frameCount % 2) + 0.5
            laserConst.colorMult = [c * 1, c * 0.1, c * 0.1, c]
            for  ff in range(len(g_fishTable)):
                fishInfo = g_fishTable[ff]
                numFish = fishInfo.num[Globals.g.globals.fishSetting]
                fishName = fishInfo.name
                scene = g_scenes[fishName]
                center = [0, g_tankHeight, 0]
                if (scene and scene.loaded and not scene.bad):
                    fish = scene.models[0]
                    mult = fish.extents.max[2] / fishInfo.constUniforms.fishLength
                    waveLength = fishInfo.constUniforms.fishWaveLength
                    bendAmount = fishInfo.constUniforms.fishBendAmount
                    for ii in range( numFish ):
                        if (fishInfo.lasers):
                            data = fishInfo.fishData[ii]
                            time = data.time
                            s = math.sin(time + mult * waveLength)
                            scale = data.scale
                            offset = mult * mult * s * bendAmount
                            off = [offset, fishInfo.laserOff[1], fishInfo.laserOff[2]]

                            scale = 1
                            fast.matrix4.mul(world,
                                             fast.matrix4.scaling(m4t1, [scale, scale, scale]),
                                             fast.matrix4.cameraLookAt(
                                                 m4t2, data.position, data.target, up))
                            fast.matrix4.mul(
                                m4t2,
                                fast.matrix4.rotationY(
                                    m4t3, s * fishInfo.laserRot),
                                fast.matrix4.translation(m4t1, off))
                            fast.matrix4.mul(
                                world,
                                m4t2,
                                world)

                            laserDir = math.normalize([world[8], world[9], world[10]])
                            point1 = [
                                world[12],
                                world[13],
                                world[14]]
                            point2 = math.addVector(
                                point1, tdl.math.mulVectorScalar(laserDir, 1000))
                            intersection = raySphereIntersection(
                                point1, point2, center, g_tankRadius)
                            if (intersection):
                                length = tdl.math.length(math.subVector(intersection, point1)) *\
                                      g_laserLenFudge
                                fast.matrix4.mul(
                                    world,
                                                fast.matrix4.scaling(
                                        m4t0,
                                        [fishInfo.laserScale[0],
                                         fishInfo.laserScale[1],
                                         length]),
                                    world)
                                fast.matrix4.mul(worldViewProjection, world, viewProjection)
                                laser.draw(laserPer)
                                surfaceNorm = math.normalize(intersection)
                                newDir = refract(
                                    math.negativeVector(laserDir), surfaceNorm, g_laserEta)
                                data.laser = {
                                    position: intersection,

                                    target:  {True: math.addVector(intersection, newDir), False: None}[newDir]
                                    }





            gl.disable(gl.BLEND)
            gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA)
            gl.enable(gl.CULL_FACE)
            gl.depthMask(True)


            if (Globals.g.options.museum.enabled):
                if (g_sceneGroups.outside):
                    Log("--Draw outside----------------")
                    DrawGroup(g_sceneGroups.outside, outsideConst, outsidePer)



            bubbleTimer -= elapsedTime * Globals.g.globals.speed
            if (bubbleTimer < 0):
                bubbleTimer = 2 + random.gauss(0.5,0.5) * 8
                radius = random.gauss(0.5,0.5) * 50
                angle = random.gauss(0.5,0.5) * math.pi * 2
                fast.matrix4.translation(
                    world,
                    [math.sin(angle) * radius,
                     0,
                     math.cos(angle) * radius])
                g_bubbleSets[bubbleIndex].trigger(world)
                bubbleIndex += 1
                bubbleIndex = bubbleIndex % g_numBubbleSets

                fast.matrix4.translation(world, [0, 0, 0])
                if (Globals.g.options.bubbles.enabled):
                    particleSystem.draw(viewProjection, world, viewInverse)


            gl.enable(gl.BLEND)
            gl.disable(gl.CULL_FACE)
            if (Globals.g.options.lightRays.enabled):
                gl.blendFunc(gl.SRC_ALPHA, gl.ONE)
                gl.depthMask(False)
                lightRay.drawPrep(lightRayConst)
                for ii in range( g_lightRayInfo.length):
                  info = g_lightRayInfo[ii]
                  lerp = info.timer / info.duration
                  y = math.max(70, math.min(120, g_lightRayY + Globals.g.globals.eyeHeight))
                  info.timer -= elapsedTime * Globals.g.globals.speed
                  if (info.timer < 0):
                      initLightRay(info)

                      fast.matrix4.mul(
                      m4t1,
                      fast.matrix4.rotationZ(m4t0, info.rot + lerp * g_lightRayRotLerp),
                      fast.matrix4.translation(m4t2, [info.x, y, 0])
                      )
                      fast.matrix4.mul(world,
                      fast.matrix4.scaling(m4t0, [10, -100, 10]),
                      m4t1
                      )
                      # compute a view with no rotation
                      fast.matrix4.translation(m4t1, [view[12], view[13], view[14]])
                      fast.matrix4.mul(m4t0, m4t1, projection)
                      fast.matrix4.mul(worldViewProjection, world, m4t0)
                      lightRayPer.colorMult[3] = math.sin(lerp * math.pi)
                      lightRay.draw(lightRayPer)



        logging.error("DREW LASERS")                    
        gl.depthMask(True)
        gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA)
        gl.blendEquation(gl.FUNC_ADD)
        
        #if (Globals.g.options.tank.enabled):
        #    if (g_sceneGroups.outer):
        #        Log("--Draw GlobeOuter----------------")
        #        DrawGroup(g_sceneGroups.outer, Globals.g.innerConst, innerPer)


        logging.error("LASERS OUT %s"%Globals.g.drawLasers)
        # Draw Lasers Outside
        if (Globals.g.drawLasers):
            Log("--Draw Lasers Outside---------------------------------------")
            gl.enable(gl.BLEND)
            gl.blendFunc(gl.ONE, gl.ONE)
            gl.disable(gl.CULL_FACE)
            gl.depthMask(False)

            laser.drawPrep(laserConst)
            for ff in range(g_fishTable.length):
                fishInfo = g_fishTable[ff]
                numFish = fishInfo.num[Globals.g.globals.fishSetting]
                fishName = fishInfo.name
                scene = g_scenes[fishName]
                if (scene and scene.loaded and not scene.bad):
                    fish = scene.models[0]
                    for ii in range(  numFish ):
                        if (fishInfo.lasers) :
                            data = fishInfo.fishData[ii]
                            laserInfo = data.laser
                            if (laserInfo.target):
                                fast.matrix4.mul(
                                world,
                                fast.matrix4.scaling(m4t1, [0.5, 0.5, 200]),
                                fast.matrix4.cameraLookAt(
                                    m4t0,
                                    laserInfo.position,
                                    laserInfo.target,
                                    up))
                                fast.matrix4.mul(worldViewProjection, world, viewProjection)
                                laser.draw(laserPer)

            gl.disable(gl.BLEND)
            gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA)
            gl.enable(gl.CULL_FACE)
            gl.depthMask(True)


        # Set the alpha to 255.
        logging.error("COLOR MASK GL %s"%gl)
        gl.colorMask(False, False, False, True)
        gl.clearColor(0,0,0,1)
        gl.clear(gl.COLOR_BUFFER_BIT)

        # turn off glogging after 1 frame.
        g_logGLCalls = False
        if (not g_drawOnce):
            assert( Globals.canvas._object())
            g_requestId = tdl.webgl.requestAnimationFrame(  render, Globals.canvas )
      except:
          import traceback
          traceback.print_exc()
          
    if not hasattr(Globals,"render"):
        Globals.render = render
    render()
    return True


#/**
# * Sets up the count buttons.
# */
def setupCountButtons():
  for ii in range( 100):
      elem = document.getElementById("setSetting" + ii)
      if (not elem):
          break
    
      g_setSettingElements.push(elem)
      def onclick( elem, id):
          def f():
              setSetting(elem, id)
          return f    
      elem.onclick = onclick(elem, ii)
  

  if (Globals.g.net.sync):
      setSetting(document.getElementById("setSetting4"), 4)
  else:
      setSetting(document.getElementById("setSetting2"), 2)
  
  setSetting(document.getElementById("setSetting9"), 9)
  


def initUIStuff():
    setupCountButtons()

    def toggleOption(name, option, elem):
        options = { }
        options[name] = {enabled:not option.enabled}
        setSettings({options:options})
        def nullf(): return
        elem.style.color = {True:"red", False:"gray"}[option.enabled]
        { 'normalMaps': setShaders,
          'reflection' : setShaders,
          'fog': setShaders,
          'tank' : nullf}[option.name]()

    optionsContainer = document.getElementById("optionsContainer")
    for name in Globals.g.options:
        option = Globals.g.options[name]
        option.name = name
        div = document.createElement('div')
        div.appendChild(document.createTextNode("-" + option.text))
        div.style.color = {True:"ref", False:"gray"}[option.enabled]
        div.setAttribute('class', "clickable")

        def toggle(name, option, div):
            def f():
                toggleOption(name, optio,div)
                return False
            return f

        option.toggle = toggle(name, option, div)
        _(div).click(option.toggle)
        def mousedown():
            return False
        div.onmousedown = mousedown
        def onstartselect():
            return False
        div.onstartselect = onstartselect
        optionsContainer.appendChild(div)
      

def init( document ):
        global _
        assert(_)
        assert( document )
        assert( Globals.g_ui)
        AddUI(Globals.g_ui)
        
        g_syncManager = tdl.sync.SyncManager(g, updateUI)
        
        if (Globals.g.get('win') and Globals.g.win.get('resize')):
            width = screen.availWidth
            height = screen.availHeight
            window.moveTo(0, 0)
            window.resizeTo(width, height)
            tdl.log("w", width, "h", height)

        
        if (Globals.g.net.get('msg') and Globals.g.net.msg.get('length')):
            _("#msgContainer").append(Globals.g.net.msg)
        else:
            _("#msgContainer").hide()
        

        if (Globals.g.net.get('sync')):
            
            Globals.g.globals.fishSetting = 4
            if (Globals.g.net.get('ui') != False):
                AddUI(g_netUI)
                _("#msgContainer").show()
            
          

        if (not Globals.g.net.get('fovFudge')) :
            
            Globals.g.net.fovFudge = 1
            Globals.g.net['fovFudge'] = 1

        def toggle():
            _("#uiContainer").toggle('slow')
            return False            
        _('#setSetting10').click(toggle)
        _("#uiContainer").toggle()
        def toggle2():
            _("#optionsContainer").toggle()
            return False
        _('#options').click(toggle2)
            
        _("#optionsContainer").toggle()
        
        if Globals.g.net.ui == False:
            _('#topUI').hide()
        else:
            def keypress(event, *args):
                return
                if (event.keyCode == 'l'.charCodeAt(0) or \
                    event.keyCode == 'L'.charCodeAt(0)):
                    setSettings({'drawLasers': not (Globals.g.drawLasers or False)})
                elif (event.keyCode == ' '.charCodeAt(0)):
                    advanceViewSettings()
                elif (event.keyCode == 's'.charCodeAt(0) or \
                      event.keyCode == 'S'.charCodeAt(0)):
                    tdl.screenshot.takeScreenshot(
                        document.getElementById("canvas"))
                elif (event.keyCode == 'h'.charCodeAt(0) or \
                      event.keyCode == 'H'.charCodeAt(0)):
                    _('#topUI').toggle()
    
            _(document).keypress(keypress)
            
        main( document )

from pyggi.javascript import jquery

def initialize_aquarium(ctxt, on_view_ready):
    global context
    context = ctxt
    assert(ctxt)
    def view_ready( *args):
        with jquery.initialize( ctxt, on_view_ready) as jq:
            global tdl
            global _
            _ = jq
            assert(_)
            tdl = context.get_jsobject("tdl")
            tdl.require('tdl.buffers')
            tdl.require('tdl.clock')
            tdl.require('tdl.fast')
            tdl.require('tdl.fps')
            tdl.require('tdl.io')
            tdl.require('tdl.log')
            tdl.require('tdl.math')
            tdl.require('tdl.models')
            tdl.require('tdl.particles')
            tdl.require('tdl.primitives')
            tdl.require('tdl.programs')
            tdl.require('tdl.sync')
            tdl.require('tdl.textures')
            tdl.require('tdl.webgl')
            document = initialize_common(context, tdl, _)
            assert(document)
            init(document)
    on_view_ready( view_ready )
