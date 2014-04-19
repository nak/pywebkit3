tdl = None
document = None
_ = None
def initialize_common( context, _tdl , jq):
    global tdl
    global document
    global _
    _ = context.get_jsobject('$')
    tdl = _tdl
    tdl.require('tdl.fast')
    tdl.require('tdl.io')
    tdl.require('tdl.log')
    tdl.require('tdl.math')
    tdl.require('tdl.screenshot')
    tdl.require('tdl.sync')
    document = context.get_jsobject("document")
    assert(document)
    return document

g_syncManager = None

g_viewSettingsIndex = 0
g_getCount = 0
g_putCount = 0
def make_object( from_dict):
    class struct(dict):

        def __getattr__(self, attr):
            return self.get(attr)
    ret = struct()
    for key,value in from_dict.items():
        if isinstance(value, dict):
            value = make_object(value)
        setattr(ret, key, value)
        ret[key] = value
    return ret

def make_objects( l ):
    for index  in range(len(l)):
        l[index] = make_object( l[index])
    return l

g_viewSettings = [
  #// Inside 1
  {
    'targetHeight': 63.3,
    'targetRadius': 91.6,
    'eyeHeight': 7.5,
    'eyeRadius': 13.2,
    'eyeSpeed': 0.0258,
    'fieldOfView': 82.699,
    'ambientRed': 0.218,
    'ambientGreen': 0.502,
    'ambientBlue': 0.706,
    'fogPower': 16.5,
    'fogMult': 1.5, #//2.02,
    'fogOffset': 0.738,
    'fogRed': 0.338,
    'fogGreen': 0.81,
    'fogBlue': 1,
    'refractionFudge': 3,
    'eta': 1,
    'tankColorFudge': 0.796
  },
  #// Outside 1
  {
    'targetHeight': 17.1,
    'targetRadius': 69.2,
    'eyeHeight': 59.1,
    'eyeRadius': 124.4,
    'eyeSpeed': 0.0258,
    'fieldOfView': 56.923,
    'ambientRed': 0.218,
    'ambientGreen': 0.246,
    'ambientBlue': 0.394,
    'fogPower': 27.1,
    'fogMult': 1.46,
    'fogOffset': 0.53,
    'fogRed': 0.382,
    'fogGreen': 0.602,
    'fogBlue': 1,
    'refractionFudge': 3,
    'eta': 1,
    'tankColorFudge': 1
  },
  #// Inside Original
  {
    'targetHeight': 0,
    'targetRadius': 88,
    'eyeHeight': 38,
    'eyeRadius': 69,
    'eyeSpeed': 0.0258,
    'fieldOfView': 64,
    'ambientRed': 0.218,
    'ambientGreen': 0.246,
    'ambientBlue': 0.394,
    'fogPower': 16.5,
    'fogMult': 1.5, #// 2.02,
    'fogOffset': 0.738,
    'fogRed': 0.338,
    'fogGreen': 0.81,
    'fogBlue': 1,
    'refractionFudge': 3,
    'eta': 1,
    'tankColorFudge': 0.796
  },
  #// Outside Original
  {
    'targetHeight': 72,
    'targetRadius': 73,
    'eyeHeight': 3.9,
    'eyeRadius': 120,
    'eyeSpeed': 0.0258,
    'fieldOfView': 74,
    'ambientRed': 0.218,
    'ambientGreen': 0.246,
    'ambientBlue': 0.394,
    'fogPower': 27.1,
    'fogMult': 1.46,
    'fogOffset': 0.53,
    'fogRed': 0.382,
    'fogGreen': 0.602,
    'fogBlue': 1,
    'refractionFudge': 3,
    'eta': 1,
    'tankColorFudge': 1
  },
  #// Center for LG
  {
    'targetHeight': 24,
    'targetRadius': 73,
    'eyeHeight': 24,
    'eyeRadius': 0,
    'eyeSpeed': 0.06,
    'fieldOfView': 60,
    'ambientRed': 0.22,
    'ambientGreen': 0.25,
    'ambientBlue': 0.39,
    'fogPower': 14.5,
    'fogMult': 1.3, #//1.66,
    'fogOffset': 0.53,
    'fogRed': 0.54,
    'fogGreen': 0.86,
    'fogBlue': 1,
    'refractionFudge': 3,
    'eta': 1,
    'tankColorFudge': 0.8
  },
  #// Outside for LG
  {
    'targetHeight': 20,
    'targetRadius': 127,
    'eyeHeight': 39.9,
    'eyeRadius': 124,
    'eyeSpeed': 0.06,
    'fieldOfView': 24,
    'ambientRed': 0.22,
    'ambientGreen': 0.25,
    'ambientBlue': 0.39,
    'fogPower': 27.1,
    'fogMult': 1.2, #//1.46,
    'fogOffset': 0.53,
    'fogRed': 0.382,
    'fogGreen': 0.602,
    'fogBlue': 1,
    'refractionFudge': 3,
    'eta': 1,
    'tankColorFudge': 1
  }
]
g_viewSettings = make_objects( g_viewSettings )

g = {
  'globals': {
    'fishSetting': 2,
    'drawLasers': False,
	'width': 1024,
	'height': 1024
  },
  'net': {
    'timeout': 3000,
    'fovMult': 1.21,
    'rotYMult': 0,
    'offsetMult': 1.0,
    'offset': [0, 0, 0],
    'port': 8080 
  },
  'win': {
    'useDevicePixelRatio': True
  },
  'fish': {},
  'innerConst': {},
  'options': {
    'normalMaps': { 'enabled': False, 'text': 'Normal Maps' },
    'reflection': { 'enabled': False, 'text': 'Reflection' },
    'tank':       { 'enabled': True,  'text': 'Tank' },
    'museum':     { 'enabled': True,  'text': 'Museum' },
    'fog':        { 'enabled': True,  'text': 'Fog' },
    'bubbles':    { 'enabled': True,  'text': 'Bubbles' },
    'lightRays':  { 'enabled': True,  'text': 'Light Rays' }
  }
}

g = make_object( g )

g_uiWidgets = {}
g_logGLCalls = True

def Log(msg):
    if (g_logGLCalls):
        tdl.log(msg)
  


def getScriptText(id):
  #//tdl.log("loading: ", id)
  elem = document.getElementById(id)
  if not elem:
    raise Exception( 'no element: ' + id)
  
  return elem.text


def updateUI(settings):
    def updateUIInner(obj, dst):
        for name in obj:
            value = obj[name]
            if isinstance( value, JSObject):
                newDst = dst[name]
                if (newDst):
                    updateUIInner(value, newDst)
                    
            else:
                elem = dst[name]
                if (elem):
                    newValue = floor(value * 1000)
                    oldValue = _(elem).slider("value")
                    if (newValue != oldValue):
                        #//tdl.log("set:", oldValue, newValue)
                        _(elem).slider("value", newValue)
    updateUIInner(settings, g_uiWidgets)


def setViewSettings(index):
    def setGlobal(name, value):
        _(g_uiWidgets.globals[name]).slider("value", value * 1000)
        g.globals[name] = value
  

    viewSettings = g_viewSettings[index]
    setSettings({globals: viewSettings})


def advanceViewSettings():
    g_viewSettingsIndex = (g_viewSettingsIndex + 1) % g_viewSettings.length
    setViewSettings(g_viewSettingsIndex)


def resetViewSettings():
    setViewSettings(g_viewSettingsIndex)


#/**
# * Sets the count
# */
def setSetting(elem, id):
    if id == 8:
        pass
    elif  id == 7:
        advanceViewSettings()
    else:
        g_numSettingElements[id] = elem
        setSettings({globals:{fishSetting:id}})
        for otherElem in g_numSettingElements:
            g_numSettingElements[otherElem].style.color = "gray"
    
        elem.style.color = "red"
  


#/**
# * Initializes stuff.
# */
def initializeCommon():
  if (g.net.sync):
      url = "ws:" + window.location.host
      tdl.log("server:", url)
      g_syncManager.init(url, g.net.slave)
      if not g.net.slave:
          g_viewSettingsIndex = 4
          setViewSettings(g_viewSettingsIndex)
    
  return True


g_event = None

def getParamId(id):
  return id.substr(6).replace("/(\w)/, function(m) {return m.toLowerCase() }")


def setParam(event, qui, ui, obj, valueElem):
  id = event.target.id
  value = qui.value / 1000
  valueElem.innerHTML = value
  inner = {}
  settings = {}
  settings[ui.obj] = inner
  inner[ui.name] = value
  setSettings(settings)


def getUIValue(obj, id):
  return obj[id] * 1000


def setupSlider(_, elem, ui, obj):
    textDiv = document.createElement('div')
    labelDiv = document.createElement('span')
    labelDiv.appendChild(document.createTextNode(ui.get('label') or ui.name))
    valueDiv = document.createElement('span')
    valueDiv.appendChild(
        document.createTextNode(getUIValue(obj, ui.name) / 1000))
    valueDiv.style.float = "right"
    sliderDiv = document.createElement('div')
    sliderDiv.id = ui.name
    textDiv.appendChild(labelDiv)
    textDiv.appendChild(valueDiv)
    elem.appendChild(textDiv)
    elem.appendChild(sliderDiv)
    if not ui.obj in g_uiWidgets:
        g_uiWidgets[ui.obj] = { }
        
    g_uiWidgets[ui.obj][ui.name] = sliderDiv
    def slide(event, qui): setParam(event, qui, ui, obj, valueDiv)
    _(sliderDiv).slider(make_object({
        'range': False,
        'step': 1,
        'max': ui.max * 1000,
        'min': (ui.get('min') or 0) * 1000,
        'value': getUIValue(obj, ui.name),
        'slide': slide
        }))


def AddUI(uiObj):
  uiElem = document.getElementById('ui')
  for  ui in uiObj:
      obj = g[ui.obj]
      if not ui.name in obj:
          obj[ui.name] = ui.value
          
      div = document.createElement('div')
      setupSlider(_, div, ui, obj)
      uiElem.appendChild(div)


def setSettings(settings):
    g_syncManager.setSettings(settings)




