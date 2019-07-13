# -*- coding: utf-8 -*-
#
#  Copyright (C) 2016 by Igor E. Novikov
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License
#  as published by the Free Software Foundation, either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

SVG_COLORS = {'aliceblue': ['RGB', [0.9411764705882353, 0.9725490196078431, 1.0], 1.0, 'aliceblue'],
'antiquewhite': ['RGB', [0.9803921568627451, 0.9215686274509803, 0.8431372549019608], 1.0, 'antiquewhite'],
'aqua': ['RGB', [0.0, 1.0, 1.0], 1.0, 'cyan'],
'aquamarine': ['RGB', [0.4980392156862745, 1.0, 0.8313725490196079], 1.0, 'aquamarine'],
'azure': ['RGB', [0.9411764705882353, 1.0, 1.0], 1.0, 'azure'],
'beige': ['RGB', [0.9607843137254902, 0.9607843137254902, 0.8627450980392157], 1.0, 'beige'],
'bisque': ['RGB', [1.0, 0.8941176470588236, 0.7686274509803922], 1.0, 'bisque'],
'black': ['RGB', [0.0, 0.0, 0.0], 1.0, 'black'],
'blanchedalmond': ['RGB', [1.0, 0.9215686274509803, 0.803921568627451], 1.0, 'blanchedalmond'],
'blue': ['RGB', [0.0, 0.0, 1.0], 1.0, 'blue'],
'blueviolet': ['RGB', [0.5411764705882353, 0.16862745098039217, 0.8862745098039215], 1.0, 'blueviolet'],
'brown': ['RGB', [0.6470588235294118, 0.16470588235294117, 0.16470588235294117], 1.0, 'brown'],
'burlywood': ['RGB', [0.8705882352941177, 0.7215686274509804, 0.5294117647058824], 1.0, 'burlywood'],
'cadetblue': ['RGB', [0.37254901960784315, 0.6196078431372549, 0.6274509803921569], 1.0, 'cadetblue'],
'chartreuse': ['RGB', [0.4980392156862745, 1.0, 0.0], 1.0, 'chartreuse'],
'chocolate': ['RGB', [0.8235294117647058, 0.4117647058823529, 0.11764705882352941], 1.0, 'chocolate'],
'coral': ['RGB', [1.0, 0.4980392156862745, 0.3137254901960784], 1.0, 'coral'],
'cornflowerblue': ['RGB', [0.39215686274509803, 0.5843137254901961, 0.9294117647058824], 1.0, 'cornflowerblue'],
'cornsilk': ['RGB', [1.0, 0.9725490196078431, 0.8627450980392157], 1.0, 'cornsilk'],
'crimson': ['RGB', [0.8627450980392157, 0.0784313725490196, 0.23529411764705882], 1.0, 'crimson'],
'cyan': ['RGB', [0.0, 1.0, 1.0], 1.0, 'cyan'],
'darkblue': ['RGB', [0.0, 0.0, 0.5450980392156862], 1.0, 'darkblue'],
'darkcyan': ['RGB', [0.0, 0.5450980392156862, 0.5450980392156862], 1.0, 'darkcyan'],
'darkgoldenrod': ['RGB', [0.7215686274509804, 0.5254901960784314, 0.043137254901960784], 1.0, 'darkgoldenrod'],
'darkgray': ['RGB', [0.6627450980392157, 0.6627450980392157, 0.6627450980392157], 1.0, 'darkgray'],
'darkgreen': ['RGB', [0.0, 0.39215686274509803, 0.0], 1.0, 'darkgreen'],
'darkgrey': ['RGB', [0.6627450980392157, 0.6627450980392157, 0.6627450980392157], 1.0, 'darkgray'],
'darkkhaki': ['RGB', [0.7411764705882353, 0.7176470588235294, 0.4196078431372549], 1.0, 'darkkhaki'],
'darkmagenta': ['RGB', [0.5450980392156862, 0.0, 0.5450980392156862], 1.0, 'darkmagenta'],
'darkolivegreen': ['RGB', [0.3333333333333333, 0.4196078431372549, 0.1843137254901961], 1.0, 'darkolivegreen'],
'darkorange': ['RGB', [1.0, 0.5490196078431373, 0.0], 1.0, 'darkorange'],
'darkorchid': ['RGB', [0.6, 0.19607843137254902, 0.8], 1.0, 'darkorchid'],
'darkred': ['RGB', [0.5450980392156862, 0.0, 0.0], 1.0, 'darkred'],
'darksalmon': ['RGB', [0.9137254901960784, 0.5882352941176471, 0.47843137254901963], 1.0, 'darksalmon'],
'darkseagreen': ['RGB', [0.5607843137254902, 0.7372549019607844, 0.5607843137254902], 1.0, 'darkseagreen'],
'darkslateblue': ['RGB', [0.2823529411764706, 0.23921568627450981, 0.5450980392156862], 1.0, 'darkslateblue'],
'darkslategray': ['RGB', [0.1843137254901961, 0.30980392156862746, 0.30980392156862746], 1.0, 'darkslategray'],
'darkslategrey': ['RGB', [0.1843137254901961, 0.30980392156862746, 0.30980392156862746], 1.0, 'darkslategray'],
'darkturquoise': ['RGB', [0.0, 0.807843137254902, 0.8196078431372549], 1.0, 'darkturquoise'],
'darkviolet': ['RGB', [0.5803921568627451, 0.0, 0.8274509803921568], 1.0, 'darkviolet'],
'deeppink': ['RGB', [1.0, 0.0784313725490196, 0.5764705882352941], 1.0, 'deeppink'],
'deepskyblue': ['RGB', [0.0, 0.7490196078431373, 1.0], 1.0, 'deepskyblue'],
'dimgray': ['RGB', [0.4117647058823529, 0.4117647058823529, 0.4117647058823529], 1.0, 'dimgray'],
'dimgrey': ['RGB', [0.4117647058823529, 0.4117647058823529, 0.4117647058823529], 1.0, 'dimgray'],
'dodgerblue': ['RGB', [0.11764705882352941, 0.5647058823529412, 1.0], 1.0, 'dodgerblue'],
'firebrick': ['RGB', [0.6980392156862745, 0.13333333333333333, 0.13333333333333333], 1.0, 'firebrick'],
'floralwhite': ['RGB', [1.0, 0.9803921568627451, 0.9411764705882353], 1.0, 'floralwhite'],
'forestgreen': ['RGB', [0.13333333333333333, 0.5450980392156862, 0.13333333333333333], 1.0, 'forestgreen'],
'fuchsia': ['RGB', [1.0, 0.0, 1.0], 1.0, 'fuchsia'],
'gainsboro': ['RGB', [0.8627450980392157, 0.8627450980392157, 0.8627450980392157], 1.0, 'gainsboro'],
'ghostwhite': ['RGB', [0.9725490196078431, 0.9725490196078431, 1.0], 1.0, 'ghostwhite'],
'gold': ['RGB', [1.0, 0.8431372549019608, 0.0], 1.0, 'gold'],
'goldenrod': ['RGB', [0.8549019607843137, 0.6470588235294118, 0.12549019607843137], 1.0, 'goldenrod'],
'gray': ['RGB', [0.5019607843137255, 0.5019607843137255, 0.5019607843137255], 1.0, 'gray'],
'green': ['RGB', [0.0, 0.5019607843137255, 0.0], 1.0, 'green'],
'greenyellow': ['RGB', [0.6784313725490196, 1.0, 0.1843137254901961], 1.0, 'greenyellow'],
'grey': ['RGB', [0.5019607843137255, 0.5019607843137255, 0.5019607843137255], 1.0, 'gray'],
'honeydew': ['RGB', [0.9411764705882353, 1.0, 0.9411764705882353], 1.0, 'honeydew'],
'hotpink': ['RGB', [1.0, 0.4117647058823529, 0.7058823529411765], 1.0, 'hotpink'],
'indianred': ['RGB', [0.803921568627451, 0.3607843137254902, 0.3607843137254902], 1.0, 'indianred'],
'indigo': ['RGB', [0.29411764705882354, 0.0, 0.5098039215686274], 1.0, 'indigo'],
'ivory': ['RGB', [1.0, 1.0, 0.9411764705882353], 1.0, 'ivory'],
'khaki': ['RGB', [0.9411764705882353, 0.9019607843137255, 0.5490196078431373], 1.0, 'khaki'],
'lavender': ['RGB', [0.9019607843137255, 0.9019607843137255, 0.9803921568627451], 1.0, 'lavender'],
'lavenderblush': ['RGB', [1.0, 0.9411764705882353, 0.9607843137254902], 1.0, 'lavenderblush'],
'lawngreen': ['RGB', [0.48627450980392156, 0.9882352941176471, 0.0], 1.0, 'lawngreen'],
'lemonchiffon': ['RGB', [1.0, 0.9803921568627451, 0.803921568627451], 1.0, 'lemonchiffon'],
'lightblue': ['RGB', [0.6784313725490196, 0.8470588235294118, 0.9019607843137255], 1.0, 'lightblue'],
'lightcoral': ['RGB', [0.9411764705882353, 0.5019607843137255, 0.5019607843137255], 1.0, 'lightcoral'],
'lightcyan': ['RGB', [0.8784313725490196, 1.0, 1.0], 1.0, 'lightcyan'],
'lightgoldenrodyellow': ['RGB', [0.9803921568627451, 0.9803921568627451, 0.8235294117647058], 1.0, 'lightgoldenrodyellow'],
'lightgray': ['RGB', [0.8274509803921568, 0.8274509803921568, 0.8274509803921568], 1.0, 'lightgray'],
'lightgreen': ['RGB', [0.5647058823529412, 0.9333333333333333, 0.5647058823529412], 1.0, 'lightgreen'],
'lightgrey': ['RGB', [0.8274509803921568, 0.8274509803921568, 0.8274509803921568], 1.0, 'lightgray'],
'lightpink': ['RGB', [1.0, 0.7137254901960784, 0.7568627450980392], 1.0, 'lightpink'],
'lightsalmon': ['RGB', [1.0, 0.6274509803921569, 0.47843137254901963], 1.0, 'lightsalmon'],
'lightseagreen': ['RGB', [0.12549019607843137, 0.6980392156862745, 0.6666666666666666], 1.0, 'lightseagreen'],
'lightskyblue': ['RGB', [0.5294117647058824, 0.807843137254902, 0.9803921568627451], 1.0, 'lightskyblue'],
'lightslategray': ['RGB', [0.4666666666666667, 0.5333333333333333, 0.6], 1.0, 'lightslategray'],
'lightslategrey': ['RGB', [0.4666666666666667, 0.5333333333333333, 0.6], 1.0, 'lightslategray'],
'lightsteelblue': ['RGB', [0.6901960784313725, 0.7686274509803922, 0.8705882352941177], 1.0, 'lightsteelblue'],
'lightyellow': ['RGB', [1.0, 1.0, 0.8784313725490196], 1.0, 'lightyellow'],
'lime': ['RGB', [0.0, 1.0, 0.0], 1.0, 'lime'],
'limegreen': ['RGB', [0.19607843137254902, 0.803921568627451, 0.19607843137254902], 1.0, 'limegreen'],
'linen': ['RGB', [0.9803921568627451, 0.9411764705882353, 0.9019607843137255], 1.0, 'linen'],
'magenta': ['RGB', [1.0, 0.0, 1.0], 1.0, 'magenta'],
'maroon': ['RGB', [0.5019607843137255, 0.0, 0.0], 1.0, 'maroon'],
'mediumaquamarine': ['RGB', [0.4, 0.803921568627451, 0.6666666666666666], 1.0, 'mediumaquamarine'],
'mediumblue': ['RGB', [0.0, 0.0, 0.803921568627451], 1.0, 'mediumblue'],
'mediumorchid': ['RGB', [0.7294117647058823, 0.3333333333333333, 0.8274509803921568], 1.0, 'mediumorchid'],
'mediumpurple': ['RGB', [0.5764705882352941, 0.4392156862745098, 0.8588235294117647], 1.0, 'mediumpurple'],
'mediumseagreen': ['RGB', [0.23529411764705882, 0.7019607843137254, 0.44313725490196076], 1.0, 'mediumseagreen'],
'mediumslateblue': ['RGB', [0.4823529411764706, 0.40784313725490196, 0.9333333333333333], 1.0, 'mediumslateblue'],
'mediumspringgreen': ['RGB', [0.0, 0.9803921568627451, 0.6039215686274509], 1.0, 'mediumspringgreen'],
'mediumturquoise': ['RGB', [0.2823529411764706, 0.8196078431372549, 0.8], 1.0, 'mediumturquoise'],
'mediumvioletred': ['RGB', [0.7803921568627451, 0.08235294117647059, 0.5215686274509804], 1.0, 'mediumvioletred'],
'midnightblue': ['RGB', [0.09803921568627451, 0.09803921568627451, 0.4392156862745098], 1.0, 'midnightblue'],
'mintcream': ['RGB', [0.9607843137254902, 1.0, 0.9803921568627451], 1.0, 'mintcream'],
'mistyrose': ['RGB', [1.0, 0.8941176470588236, 0.8823529411764706], 1.0, 'mistyrose'],
'moccasin': ['RGB', [1.0, 0.8941176470588236, 0.7098039215686275], 1.0, 'moccasin'],
'navajowhite': ['RGB', [1.0, 0.8705882352941177, 0.6784313725490196], 1.0, 'navajowhite'],
'navy': ['RGB', [0.0, 0.0, 0.5019607843137255], 1.0, 'navy'],
'oldlace': ['RGB', [0.9921568627450981, 0.9607843137254902, 0.9019607843137255], 1.0, 'oldlace'],
'olive': ['RGB', [0.5019607843137255, 0.5019607843137255, 0.0], 1.0, 'olive'],
'olivedrab': ['RGB', [0.4196078431372549, 0.5568627450980392, 0.13725490196078433], 1.0, 'olivedrab'],
'orange': ['RGB', [1.0, 0.6470588235294118, 0.0], 1.0, 'orange'],
'orangered': ['RGB', [1.0, 0.27058823529411763, 0.0], 1.0, 'orangered'],
'orchid': ['RGB', [0.8549019607843137, 0.4392156862745098, 0.8392156862745098], 1.0, 'orchid'],
'palegoldenrod': ['RGB', [0.9333333333333333, 0.9098039215686274, 0.6666666666666666], 1.0, 'palegoldenrod'],
'palegreen': ['RGB', [0.596078431372549, 0.984313725490196, 0.596078431372549], 1.0, 'palegreen'],
'paleturquoise': ['RGB', [0.6862745098039216, 0.9333333333333333, 0.9333333333333333], 1.0, 'paleturquoise'],
'palevioletred': ['RGB', [0.8588235294117647, 0.4392156862745098, 0.5764705882352941], 1.0, 'palevioletred'],
'papayawhip': ['RGB', [1.0, 0.9372549019607843, 0.8352941176470589], 1.0, 'papayawhip'],
'peachpuff': ['RGB', [1.0, 0.8549019607843137, 0.7254901960784313], 1.0, 'peachpuff'],
'peru': ['RGB', [0.803921568627451, 0.5215686274509804, 0.24705882352941178], 1.0, 'per'],
'pink': ['RGB', [1.0, 0.7529411764705882, 0.796078431372549], 1.0, 'pink'],
'plum': ['RGB', [0.8666666666666667, 0.6274509803921569, 0.8666666666666667], 1.0, 'plum'],
'powderblue': ['RGB', [0.6901960784313725, 0.8784313725490196, 0.9019607843137255], 1.0, 'powderblue'],
'purple': ['RGB', [0.5019607843137255, 0.0, 0.5019607843137255], 1.0, 'purple'],
'red': ['RGB', [1.0, 0.0, 0.0], 1.0, 'red'],
'rosybrown': ['RGB', [0.7372549019607844, 0.5607843137254902, 0.5607843137254902], 1.0, 'rosybrown'],
'royalblue': ['RGB', [0.2549019607843137, 0.4117647058823529, 0.8823529411764706], 1.0, 'royalblue'],
'saddlebrown': ['RGB', [0.5450980392156862, 0.27058823529411763, 0.07450980392156863], 1.0, 'saddlebrown'],
'salmon': ['RGB', [0.9803921568627451, 0.5019607843137255, 0.4470588235294118], 1.0, 'salmon'],
'sandybrown': ['RGB', [0.9568627450980393, 0.6431372549019608, 0.3764705882352941], 1.0, 'sandybrown'],
'seagreen': ['RGB', [0.1803921568627451, 0.5450980392156862, 0.3411764705882353], 1.0, 'seagreen'],
'seashell': ['RGB', [1.0, 0.9607843137254902, 0.9333333333333333], 1.0, 'seashell'],
'sienna': ['RGB', [0.6274509803921569, 0.3215686274509804, 0.17647058823529413], 1.0, 'sienna'],
'silver': ['RGB', [0.7529411764705882, 0.7529411764705882, 0.7529411764705882], 1.0, 'silver'],
'skyblue': ['RGB', [0.5294117647058824, 0.807843137254902, 0.9215686274509803], 1.0, 'skyblue'],
'slateblue': ['RGB', [0.41568627450980394, 0.35294117647058826, 0.803921568627451], 1.0, 'slateblue'],
'slategray': ['RGB', [0.4392156862745098, 0.5019607843137255, 0.5647058823529412], 1.0, 'slategray'],
'slategrey': ['RGB', [0.4392156862745098, 0.5019607843137255, 0.5647058823529412], 1.0, 'slategray'],
'snow': ['RGB', [1.0, 0.9803921568627451, 0.9803921568627451], 1.0, 'snow'],
'springgreen': ['RGB', [0.0, 1.0, 0.4980392156862745], 1.0, 'springgreen'],
'steelblue': ['RGB', [0.27450980392156865, 0.5098039215686274, 0.7058823529411765], 1.0, 'steelblue'],
'tan': ['RGB', [0.8235294117647058, 0.7058823529411765, 0.5490196078431373], 1.0, 'tan'],
'teal': ['RGB', [0.0, 0.5019607843137255, 0.5019607843137255], 1.0, 'teal'],
'thistle': ['RGB', [0.8470588235294118, 0.7490196078431373, 0.8470588235294118], 1.0, 'thistle'],
'tomato': ['RGB', [1.0, 0.38823529411764707, 0.2784313725490196], 1.0, 'tomato'],
'turquoise': ['RGB', [0.25098039215686274, 0.8784313725490196, 0.8156862745098039], 1.0, 'turquoise'],
'violet': ['RGB', [0.9333333333333333, 0.5098039215686274, 0.9333333333333333], 1.0, 'violet'],
'wheat': ['RGB', [0.9607843137254902, 0.8705882352941177, 0.7019607843137254], 1.0, 'wheat'],
'white': ['RGB', [1.0, 1.0, 1.0], 1.0, 'white'],
'whitesmoke': ['RGB', [0.9607843137254902, 0.9607843137254902, 0.9607843137254902], 1.0, 'whitesmoke'],
'yellow': ['RGB', [1.0, 1.0, 0.0], 1.0, 'yellow'],
'yellowgreen': ['RGB', [0.6039215686274509, 0.803921568627451, 0.19607843137254902], 1.0, 'yellowgreen'],
}
