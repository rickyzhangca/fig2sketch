[
    {
        "name": "MessageType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "JOIN_START", "type": 0, "array": False, "value": 0},
                1: {"name": "NODE_CHANGES", "type": 0, "array": False, "value": 1},
                2: {"name": "USER_CHANGES", "type": 0, "array": False, "value": 2},
                3: {"name": "JOIN_END", "type": 0, "array": False, "value": 3},
                4: {"name": "SIGNAL", "type": 0, "array": False, "value": 4},
                5: {"name": "STYLE", "type": 0, "array": False, "value": 5},
                6: {"name": "STYLE_SET", "type": 0, "array": False, "value": 6},
                7: {"name": "JOIN_START_SKIP_RELOAD", "type": 0, "array": False, "value": 7},
                8: {"name": "NOTIFY_SHOULD_UPGRADE", "type": 0, "array": False, "value": 8},
                9: {"name": "UPGRADE_DONE", "type": 0, "array": False, "value": 9},
                10: {"name": "UPGRADE_REFRESH", "type": 0, "array": False, "value": 10},
                11: {"name": "SCENE_GRAPH_QUERY", "type": 0, "array": False, "value": 11},
                12: {"name": "SCENE_GRAPH_REPLY", "type": 0, "array": False, "value": 12},
                13: {"name": "DIFF", "type": 0, "array": False, "value": 13},
                14: {"name": "CLIENT_BROADCAST", "type": 0, "array": False, "value": 14},
                15: {"name": "JOIN_START_JOURNALED", "type": 0, "array": False, "value": 15},
                16: {"name": "STREAM_START", "type": 0, "array": False, "value": 16},
                17: {"name": "STREAM_END", "type": 0, "array": False, "value": 17},
                18: {"name": "INTERACTIVE_SLIDE_CHANGE", "type": 0, "array": False, "value": 18},
            }
        ),
    },
    {
        "name": "Axis",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "X", "type": 0, "array": False, "value": 0},
                1: {"name": "Y", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "Access",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "READ_ONLY", "type": 0, "array": False, "value": 0},
                1: {"name": "READ_WRITE", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "NodePhase",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "CREATED", "type": 0, "array": False, "value": 0},
                1: {"name": "REMOVED", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "WindingRule",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONZERO", "type": 0, "array": False, "value": 0},
                1: {"name": "ODD", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "NodeType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "DOCUMENT", "type": 0, "array": False, "value": 1},
                2: {"name": "CANVAS", "type": 0, "array": False, "value": 2},
                3: {"name": "GROUP", "type": 0, "array": False, "value": 3},
                4: {"name": "FRAME", "type": 0, "array": False, "value": 4},
                5: {"name": "BOOLEAN_OPERATION", "type": 0, "array": False, "value": 5},
                6: {"name": "VECTOR", "type": 0, "array": False, "value": 6},
                7: {"name": "STAR", "type": 0, "array": False, "value": 7},
                8: {"name": "LINE", "type": 0, "array": False, "value": 8},
                9: {"name": "ELLIPSE", "type": 0, "array": False, "value": 9},
                10: {"name": "RECTANGLE", "type": 0, "array": False, "value": 10},
                11: {"name": "REGULAR_POLYGON", "type": 0, "array": False, "value": 11},
                12: {"name": "ROUNDED_RECTANGLE", "type": 0, "array": False, "value": 12},
                13: {"name": "TEXT", "type": 0, "array": False, "value": 13},
                14: {"name": "SLICE", "type": 0, "array": False, "value": 14},
                15: {"name": "SYMBOL", "type": 0, "array": False, "value": 15},
                16: {"name": "INSTANCE", "type": 0, "array": False, "value": 16},
                17: {"name": "STICKY", "type": 0, "array": False, "value": 17},
                18: {"name": "SHAPE_WITH_TEXT", "type": 0, "array": False, "value": 18},
                19: {"name": "CONNECTOR", "type": 0, "array": False, "value": 19},
                20: {"name": "CODE_BLOCK", "type": 0, "array": False, "value": 20},
                21: {"name": "WIDGET", "type": 0, "array": False, "value": 21},
                22: {"name": "STAMP", "type": 0, "array": False, "value": 22},
                23: {"name": "MEDIA", "type": 0, "array": False, "value": 23},
                24: {"name": "HIGHLIGHT", "type": 0, "array": False, "value": 24},
                25: {"name": "SECTION", "type": 0, "array": False, "value": 25},
                26: {"name": "SECTION_OVERLAY", "type": 0, "array": False, "value": 26},
                27: {"name": "WASHI_TAPE", "type": 0, "array": False, "value": 27},
                28: {"name": "VARIABLE", "type": 0, "array": False, "value": 28},
                29: {"name": "TABLE", "type": 0, "array": False, "value": 29},
                30: {"name": "TABLE_CELL", "type": 0, "array": False, "value": 30},
                31: {"name": "VARIABLE_SET", "type": 0, "array": False, "value": 31},
                32: {"name": "SLIDE", "type": 0, "array": False, "value": 32},
                33: {"name": "ASSISTED_LAYOUT", "type": 0, "array": False, "value": 33},
                34: {"name": "INTERACTIVE_SLIDE_ELEMENT", "type": 0, "array": False, "value": 34},
                35: {"name": "VARIABLE_OVERRIDE", "type": 0, "array": False, "value": 35},
                36: {"name": "MODULE", "type": 0, "array": False, "value": 36},
            }
        ),
    },
    {
        "name": "ShapeWithTextType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "SQUARE", "type": 0, "array": False, "value": 0},
                1: {"name": "ELLIPSE", "type": 0, "array": False, "value": 1},
                2: {"name": "DIAMOND", "type": 0, "array": False, "value": 2},
                3: {"name": "TRIANGLE_UP", "type": 0, "array": False, "value": 3},
                4: {"name": "TRIANGLE_DOWN", "type": 0, "array": False, "value": 4},
                5: {"name": "ROUNDED_RECTANGLE", "type": 0, "array": False, "value": 5},
                6: {"name": "PARALLELOGRAM_RIGHT", "type": 0, "array": False, "value": 6},
                7: {"name": "PARALLELOGRAM_LEFT", "type": 0, "array": False, "value": 7},
                8: {"name": "ENG_DATABASE", "type": 0, "array": False, "value": 8},
                9: {"name": "ENG_QUEUE", "type": 0, "array": False, "value": 9},
                10: {"name": "ENG_FILE", "type": 0, "array": False, "value": 10},
                11: {"name": "ENG_FOLDER", "type": 0, "array": False, "value": 11},
                12: {"name": "TRAPEZOID", "type": 0, "array": False, "value": 12},
                13: {"name": "PREDEFINED_PROCESS", "type": 0, "array": False, "value": 13},
                14: {"name": "SHIELD", "type": 0, "array": False, "value": 14},
                15: {"name": "DOCUMENT_SINGLE", "type": 0, "array": False, "value": 15},
                16: {"name": "DOCUMENT_MULTIPLE", "type": 0, "array": False, "value": 16},
                17: {"name": "MANUAL_INPUT", "type": 0, "array": False, "value": 17},
                18: {"name": "HEXAGON", "type": 0, "array": False, "value": 18},
                19: {"name": "CHEVRON", "type": 0, "array": False, "value": 19},
                20: {"name": "PENTAGON", "type": 0, "array": False, "value": 20},
                21: {"name": "OCTAGON", "type": 0, "array": False, "value": 21},
                22: {"name": "STAR", "type": 0, "array": False, "value": 22},
                23: {"name": "PLUS", "type": 0, "array": False, "value": 23},
                24: {"name": "ARROW_LEFT", "type": 0, "array": False, "value": 24},
                25: {"name": "ARROW_RIGHT", "type": 0, "array": False, "value": 25},
                26: {"name": "SUMMING_JUNCTION", "type": 0, "array": False, "value": 26},
                27: {"name": "OR", "type": 0, "array": False, "value": 27},
                28: {"name": "SPEECH_BUBBLE", "type": 0, "array": False, "value": 28},
                29: {"name": "INTERNAL_STORAGE", "type": 0, "array": False, "value": 29},
            }
        ),
    },
    {
        "name": "BlendMode",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "PASS_THROUGH", "type": 0, "array": False, "value": 0},
                1: {"name": "NORMAL", "type": 0, "array": False, "value": 1},
                2: {"name": "DARKEN", "type": 0, "array": False, "value": 2},
                3: {"name": "MULTIPLY", "type": 0, "array": False, "value": 3},
                4: {"name": "LINEAR_BURN", "type": 0, "array": False, "value": 4},
                5: {"name": "COLOR_BURN", "type": 0, "array": False, "value": 5},
                6: {"name": "LIGHTEN", "type": 0, "array": False, "value": 6},
                7: {"name": "SCREEN", "type": 0, "array": False, "value": 7},
                8: {"name": "LINEAR_DODGE", "type": 0, "array": False, "value": 8},
                9: {"name": "COLOR_DODGE", "type": 0, "array": False, "value": 9},
                10: {"name": "OVERLAY", "type": 0, "array": False, "value": 10},
                11: {"name": "SOFT_LIGHT", "type": 0, "array": False, "value": 11},
                12: {"name": "HARD_LIGHT", "type": 0, "array": False, "value": 12},
                13: {"name": "DIFFERENCE", "type": 0, "array": False, "value": 13},
                14: {"name": "EXCLUSION", "type": 0, "array": False, "value": 14},
                15: {"name": "HUE", "type": 0, "array": False, "value": 15},
                16: {"name": "SATURATION", "type": 0, "array": False, "value": 16},
                17: {"name": "COLOR", "type": 0, "array": False, "value": 17},
                18: {"name": "LUMINOSITY", "type": 0, "array": False, "value": 18},
            }
        ),
    },
    {
        "name": "PaintType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "SOLID", "type": 0, "array": False, "value": 0},
                1: {"name": "GRADIENT_LINEAR", "type": 0, "array": False, "value": 1},
                2: {"name": "GRADIENT_RADIAL", "type": 0, "array": False, "value": 2},
                3: {"name": "GRADIENT_ANGULAR", "type": 0, "array": False, "value": 3},
                4: {"name": "GRADIENT_DIAMOND", "type": 0, "array": False, "value": 4},
                5: {"name": "IMAGE", "type": 0, "array": False, "value": 5},
                6: {"name": "EMOJI", "type": 0, "array": False, "value": 6},
                7: {"name": "VIDEO", "type": 0, "array": False, "value": 7},
            }
        ),
    },
    {
        "name": "ImageScaleMode",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "STRETCH", "type": 0, "array": False, "value": 0},
                1: {"name": "FIT", "type": 0, "array": False, "value": 1},
                2: {"name": "FILL", "type": 0, "array": False, "value": 2},
                3: {"name": "TILE", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "EffectType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "INNER_SHADOW", "type": 0, "array": False, "value": 0},
                1: {"name": "DROP_SHADOW", "type": 0, "array": False, "value": 1},
                2: {"name": "FOREGROUND_BLUR", "type": 0, "array": False, "value": 2},
                3: {"name": "BACKGROUND_BLUR", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "TextCase",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "ORIGINAL", "type": 0, "array": False, "value": 0},
                1: {"name": "UPPER", "type": 0, "array": False, "value": 1},
                2: {"name": "LOWER", "type": 0, "array": False, "value": 2},
                3: {"name": "TITLE", "type": 0, "array": False, "value": 3},
                4: {"name": "SMALL_CAPS", "type": 0, "array": False, "value": 4},
                5: {"name": "SMALL_CAPS_FORCED", "type": 0, "array": False, "value": 5},
            }
        ),
    },
    {
        "name": "TextDecoration",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "UNDERLINE", "type": 0, "array": False, "value": 1},
                2: {"name": "STRIKETHROUGH", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "LeadingTrim",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "CAP_HEIGHT", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "NumberUnits",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "RAW", "type": 0, "array": False, "value": 0},
                1: {"name": "PIXELS", "type": 0, "array": False, "value": 1},
                2: {"name": "PERCENT", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ConstraintType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "MIN", "type": 0, "array": False, "value": 0},
                1: {"name": "CENTER", "type": 0, "array": False, "value": 1},
                2: {"name": "MAX", "type": 0, "array": False, "value": 2},
                3: {"name": "STRETCH", "type": 0, "array": False, "value": 3},
                4: {"name": "SCALE", "type": 0, "array": False, "value": 4},
                5: {"name": "FIXED_MIN", "type": 0, "array": False, "value": 5},
                6: {"name": "FIXED_MAX", "type": 0, "array": False, "value": 6},
            }
        ),
    },
    {
        "name": "StrokeAlign",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "CENTER", "type": 0, "array": False, "value": 0},
                1: {"name": "INSIDE", "type": 0, "array": False, "value": 1},
                2: {"name": "OUTSIDE", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "StrokeCap",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "ROUND", "type": 0, "array": False, "value": 1},
                2: {"name": "SQUARE", "type": 0, "array": False, "value": 2},
                3: {"name": "ARROW_LINES", "type": 0, "array": False, "value": 3},
                4: {"name": "ARROW_EQUILATERAL", "type": 0, "array": False, "value": 4},
                5: {"name": "DIAMOND_FILLED", "type": 0, "array": False, "value": 5},
                6: {"name": "TRIANGLE_FILLED", "type": 0, "array": False, "value": 6},
                7: {"name": "HIGHLIGHT", "type": 0, "array": False, "value": 7},
                8: {"name": "WASHI_TAPE_1", "type": 0, "array": False, "value": 8},
                9: {"name": "WASHI_TAPE_2", "type": 0, "array": False, "value": 9},
                10: {"name": "WASHI_TAPE_3", "type": 0, "array": False, "value": 10},
                11: {"name": "WASHI_TAPE_4", "type": 0, "array": False, "value": 11},
                12: {"name": "WASHI_TAPE_5", "type": 0, "array": False, "value": 12},
                13: {"name": "WASHI_TAPE_6", "type": 0, "array": False, "value": 13},
                14: {"name": "CIRCLE_FILLED", "type": 0, "array": False, "value": 14},
            }
        ),
    },
    {
        "name": "StrokeJoin",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "MITER", "type": 0, "array": False, "value": 0},
                1: {"name": "BEVEL", "type": 0, "array": False, "value": 1},
                2: {"name": "ROUND", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "BooleanOperation",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "UNION", "type": 0, "array": False, "value": 0},
                1: {"name": "INTERSECT", "type": 0, "array": False, "value": 1},
                2: {"name": "SUBTRACT", "type": 0, "array": False, "value": 2},
                3: {"name": "XOR", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "TextAlignHorizontal",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "LEFT", "type": 0, "array": False, "value": 0},
                1: {"name": "CENTER", "type": 0, "array": False, "value": 1},
                2: {"name": "RIGHT", "type": 0, "array": False, "value": 2},
                3: {"name": "JUSTIFIED", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "TextAlignVertical",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "TOP", "type": 0, "array": False, "value": 0},
                1: {"name": "CENTER", "type": 0, "array": False, "value": 1},
                2: {"name": "BOTTOM", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "MouseCursor",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "DEFAULT", "type": 0, "array": False, "value": 0},
                1: {"name": "CROSSHAIR", "type": 0, "array": False, "value": 1},
                2: {"name": "EYEDROPPER", "type": 0, "array": False, "value": 2},
                3: {"name": "HAND", "type": 0, "array": False, "value": 3},
                4: {"name": "PAINT_BUCKET", "type": 0, "array": False, "value": 4},
                5: {"name": "PEN", "type": 0, "array": False, "value": 5},
                6: {"name": "PENCIL", "type": 0, "array": False, "value": 6},
                7: {"name": "MARKER", "type": 0, "array": False, "value": 7},
                8: {"name": "ERASER", "type": 0, "array": False, "value": 8},
                9: {"name": "HIGHLIGHTER", "type": 0, "array": False, "value": 9},
            }
        ),
    },
    {
        "name": "VectorMirror",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "ANGLE", "type": 0, "array": False, "value": 1},
                2: {"name": "ANGLE_AND_LENGTH", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "DashMode",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "CLIP", "type": 0, "array": False, "value": 0},
                1: {"name": "STRETCH", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "ImageType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "PNG", "type": 0, "array": False, "value": 0},
                1: {"name": "JPEG", "type": 0, "array": False, "value": 1},
                2: {"name": "SVG", "type": 0, "array": False, "value": 2},
                3: {"name": "PDF", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "ExportConstraintType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "CONTENT_SCALE", "type": 0, "array": False, "value": 0},
                1: {"name": "CONTENT_WIDTH", "type": 0, "array": False, "value": 1},
                2: {"name": "CONTENT_HEIGHT", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "LayoutGridType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "MIN", "type": 0, "array": False, "value": 0},
                1: {"name": "CENTER", "type": 0, "array": False, "value": 1},
                2: {"name": "STRETCH", "type": 0, "array": False, "value": 2},
                3: {"name": "MAX", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "LayoutGridPattern",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "STRIPES", "type": 0, "array": False, "value": 0},
                1: {"name": "GRID", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "TextAutoResize",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "WIDTH_AND_HEIGHT", "type": 0, "array": False, "value": 1},
                2: {"name": "HEIGHT", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "TextTruncation",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "DISABLED", "type": 0, "array": False, "value": 0},
                1: {"name": "ENDING", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "StyleSetType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "PERSONAL", "type": 0, "array": False, "value": 0},
                1: {"name": "TEAM", "type": 0, "array": False, "value": 1},
                2: {"name": "CUSTOM", "type": 0, "array": False, "value": 2},
                3: {"name": "FREQUENCY", "type": 0, "array": False, "value": 3},
                4: {"name": "TEMPORARY", "type": 0, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "StyleSetContentType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "SOLID", "type": 0, "array": False, "value": 0},
                1: {"name": "GRADIENT", "type": 0, "array": False, "value": 1},
                2: {"name": "IMAGE", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "StackMode",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "HORIZONTAL", "type": 0, "array": False, "value": 1},
                2: {"name": "VERTICAL", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "StackAlign",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "MIN", "type": 0, "array": False, "value": 0},
                1: {"name": "CENTER", "type": 0, "array": False, "value": 1},
                2: {"name": "MAX", "type": 0, "array": False, "value": 2},
                3: {"name": "BASELINE", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "StackCounterAlign",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "MIN", "type": 0, "array": False, "value": 0},
                1: {"name": "CENTER", "type": 0, "array": False, "value": 1},
                2: {"name": "MAX", "type": 0, "array": False, "value": 2},
                3: {"name": "STRETCH", "type": 0, "array": False, "value": 3},
                4: {"name": "AUTO", "type": 0, "array": False, "value": 4},
                5: {"name": "BASELINE", "type": 0, "array": False, "value": 5},
            }
        ),
    },
    {
        "name": "StackJustify",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "MIN", "type": 0, "array": False, "value": 0},
                1: {"name": "CENTER", "type": 0, "array": False, "value": 1},
                2: {"name": "MAX", "type": 0, "array": False, "value": 2},
                3: {"name": "SPACE_EVENLY", "type": 0, "array": False, "value": 3},
                4: {"name": "SPACE_BETWEEN", "type": 0, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "StackSize",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "FIXED", "type": 0, "array": False, "value": 0},
                1: {"name": "RESIZE_TO_FIT", "type": 0, "array": False, "value": 1},
                2: {
                    "name": "RESIZE_TO_FIT_WITH_IMPLICIT_SIZE",
                    "type": 0,
                    "array": False,
                    "value": 2,
                },
            }
        ),
    },
    {
        "name": "StackPositioning",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "AUTO", "type": 0, "array": False, "value": 0},
                1: {"name": "ABSOLUTE", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "StackWrap",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NO_WRAP", "type": 0, "array": False, "value": 0},
                1: {"name": "WRAP", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "StackCounterAlignContent",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "AUTO", "type": 0, "array": False, "value": 0},
                1: {"name": "SPACE_BETWEEN", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "ConnectionType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "INTERNAL_NODE", "type": 0, "array": False, "value": 1},
                2: {"name": "URL", "type": 0, "array": False, "value": 2},
                3: {"name": "BACK", "type": 0, "array": False, "value": 3},
                4: {"name": "CLOSE", "type": 0, "array": False, "value": 4},
                5: {"name": "SET_VARIABLE", "type": 0, "array": False, "value": 5},
                6: {"name": "UPDATE_MEDIA_RUNTIME", "type": 0, "array": False, "value": 6},
                7: {"name": "CONDITIONAL", "type": 0, "array": False, "value": 7},
            }
        ),
    },
    {
        "name": "InteractionType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "ON_CLICK", "type": 0, "array": False, "value": 0},
                1: {"name": "AFTER_TIMEOUT", "type": 0, "array": False, "value": 1},
                2: {"name": "MOUSE_IN", "type": 0, "array": False, "value": 2},
                3: {"name": "MOUSE_OUT", "type": 0, "array": False, "value": 3},
                4: {"name": "ON_HOVER", "type": 0, "array": False, "value": 4},
                5: {"name": "MOUSE_DOWN", "type": 0, "array": False, "value": 5},
                6: {"name": "MOUSE_UP", "type": 0, "array": False, "value": 6},
                7: {"name": "ON_PRESS", "type": 0, "array": False, "value": 7},
                8: {"name": "NONE", "type": 0, "array": False, "value": 8},
                9: {"name": "DRAG", "type": 0, "array": False, "value": 9},
                10: {"name": "ON_KEY_DOWN", "type": 0, "array": False, "value": 10},
                11: {"name": "ON_VOICE", "type": 0, "array": False, "value": 11},
                12: {"name": "ON_MEDIA_HIT", "type": 0, "array": False, "value": 12},
                13: {"name": "ON_MEDIA_END", "type": 0, "array": False, "value": 13},
                14: {"name": "MOUSE_ENTER", "type": 0, "array": False, "value": 14},
                15: {"name": "MOUSE_LEAVE", "type": 0, "array": False, "value": 15},
            }
        ),
    },
    {
        "name": "TransitionType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "INSTANT_TRANSITION", "type": 0, "array": False, "value": 0},
                1: {"name": "DISSOLVE", "type": 0, "array": False, "value": 1},
                2: {"name": "FADE", "type": 0, "array": False, "value": 2},
                3: {"name": "SLIDE_FROM_LEFT", "type": 0, "array": False, "value": 3},
                4: {"name": "SLIDE_FROM_RIGHT", "type": 0, "array": False, "value": 4},
                5: {"name": "SLIDE_FROM_TOP", "type": 0, "array": False, "value": 5},
                6: {"name": "SLIDE_FROM_BOTTOM", "type": 0, "array": False, "value": 6},
                7: {"name": "PUSH_FROM_LEFT", "type": 0, "array": False, "value": 7},
                8: {"name": "PUSH_FROM_RIGHT", "type": 0, "array": False, "value": 8},
                9: {"name": "PUSH_FROM_TOP", "type": 0, "array": False, "value": 9},
                10: {"name": "PUSH_FROM_BOTTOM", "type": 0, "array": False, "value": 10},
                11: {"name": "MOVE_FROM_LEFT", "type": 0, "array": False, "value": 11},
                12: {"name": "MOVE_FROM_RIGHT", "type": 0, "array": False, "value": 12},
                13: {"name": "MOVE_FROM_TOP", "type": 0, "array": False, "value": 13},
                14: {"name": "MOVE_FROM_BOTTOM", "type": 0, "array": False, "value": 14},
                15: {"name": "SLIDE_OUT_TO_LEFT", "type": 0, "array": False, "value": 15},
                16: {"name": "SLIDE_OUT_TO_RIGHT", "type": 0, "array": False, "value": 16},
                17: {"name": "SLIDE_OUT_TO_TOP", "type": 0, "array": False, "value": 17},
                18: {"name": "SLIDE_OUT_TO_BOTTOM", "type": 0, "array": False, "value": 18},
                19: {"name": "MOVE_OUT_TO_LEFT", "type": 0, "array": False, "value": 19},
                20: {"name": "MOVE_OUT_TO_RIGHT", "type": 0, "array": False, "value": 20},
                21: {"name": "MOVE_OUT_TO_TOP", "type": 0, "array": False, "value": 21},
                22: {"name": "MOVE_OUT_TO_BOTTOM", "type": 0, "array": False, "value": 22},
                23: {"name": "MAGIC_MOVE", "type": 0, "array": False, "value": 23},
                24: {"name": "SMART_ANIMATE", "type": 0, "array": False, "value": 24},
                25: {"name": "SCROLL_ANIMATE", "type": 0, "array": False, "value": 25},
            }
        ),
    },
    {
        "name": "EasingType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "IN_CUBIC", "type": 0, "array": False, "value": 0},
                1: {"name": "OUT_CUBIC", "type": 0, "array": False, "value": 1},
                2: {"name": "INOUT_CUBIC", "type": 0, "array": False, "value": 2},
                3: {"name": "LINEAR", "type": 0, "array": False, "value": 3},
                4: {"name": "IN_BACK_CUBIC", "type": 0, "array": False, "value": 4},
                5: {"name": "OUT_BACK_CUBIC", "type": 0, "array": False, "value": 5},
                6: {"name": "INOUT_BACK_CUBIC", "type": 0, "array": False, "value": 6},
                7: {"name": "CUSTOM_CUBIC", "type": 0, "array": False, "value": 7},
                8: {"name": "SPRING", "type": 0, "array": False, "value": 8},
                9: {"name": "GENTLE_SPRING", "type": 0, "array": False, "value": 9},
                10: {"name": "CUSTOM_SPRING", "type": 0, "array": False, "value": 10},
                11: {"name": "SPRING_PRESET_ONE", "type": 0, "array": False, "value": 11},
                12: {"name": "SPRING_PRESET_TWO", "type": 0, "array": False, "value": 12},
                13: {"name": "SPRING_PRESET_THREE", "type": 0, "array": False, "value": 13},
            }
        ),
    },
    {
        "name": "ScrollDirection",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "HORIZONTAL", "type": 0, "array": False, "value": 1},
                2: {"name": "VERTICAL", "type": 0, "array": False, "value": 2},
                3: {"name": "BOTH", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "ScrollContractedState",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "EXPANDED", "type": 0, "array": False, "value": 0},
                1: {"name": "CONTRACTED", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "GUID",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "sessionID", "type": -4, "array": False, "value": 1},
                2: {"name": "localID", "type": -4, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "Color",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "r", "type": -5, "array": False, "value": 1},
                2: {"name": "g", "type": -5, "array": False, "value": 2},
                3: {"name": "b", "type": -5, "array": False, "value": 3},
                4: {"name": "a", "type": -5, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "Vector",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "x", "type": -5, "array": False, "value": 1},
                2: {"name": "y", "type": -5, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "Rect",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "x", "type": -5, "array": False, "value": 1},
                2: {"name": "y", "type": -5, "array": False, "value": 2},
                3: {"name": "w", "type": -5, "array": False, "value": 3},
                4: {"name": "h", "type": -5, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "ColorStop",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "color", "type": 48, "array": False, "value": 1},
                2: {"name": "position", "type": -5, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "Matrix",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "m00", "type": -5, "array": False, "value": 1},
                2: {"name": "m01", "type": -5, "array": False, "value": 2},
                3: {"name": "m02", "type": -5, "array": False, "value": 3},
                4: {"name": "m10", "type": -5, "array": False, "value": 4},
                5: {"name": "m11", "type": -5, "array": False, "value": 5},
                6: {"name": "m12", "type": -5, "array": False, "value": 6},
            }
        ),
    },
    {
        "name": "ParentIndex",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                2: {"name": "position", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "Number",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "value", "type": -5, "array": False, "value": 1},
                2: {"name": "units", "type": 14, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "FontName",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "family", "type": -6, "array": False, "value": 1},
                2: {"name": "style", "type": -6, "array": False, "value": 2},
                3: {"name": "postscript", "type": -6, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "FontVariantNumericFigure",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NORMAL", "type": 0, "array": False, "value": 0},
                1: {"name": "LINING", "type": 0, "array": False, "value": 1},
                2: {"name": "OLDSTYLE", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "FontVariantNumericSpacing",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NORMAL", "type": 0, "array": False, "value": 0},
                1: {"name": "PROPORTIONAL", "type": 0, "array": False, "value": 1},
                2: {"name": "TABULAR", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "FontVariantNumericFraction",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NORMAL", "type": 0, "array": False, "value": 0},
                1: {"name": "DIAGONAL", "type": 0, "array": False, "value": 1},
                2: {"name": "STACKED", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "FontVariantCaps",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NORMAL", "type": 0, "array": False, "value": 0},
                1: {"name": "SMALL", "type": 0, "array": False, "value": 1},
                2: {"name": "ALL_SMALL", "type": 0, "array": False, "value": 2},
                3: {"name": "PETITE", "type": 0, "array": False, "value": 3},
                4: {"name": "ALL_PETITE", "type": 0, "array": False, "value": 4},
                5: {"name": "UNICASE", "type": 0, "array": False, "value": 5},
                6: {"name": "TITLING", "type": 0, "array": False, "value": 6},
            }
        ),
    },
    {
        "name": "FontVariantPosition",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NORMAL", "type": 0, "array": False, "value": 0},
                1: {"name": "SUB", "type": 0, "array": False, "value": 1},
                2: {"name": "SUPER", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "FontStyle",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NORMAL", "type": 0, "array": False, "value": 0},
                1: {"name": "ITALIC", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "SemanticWeight",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NORMAL", "type": 0, "array": False, "value": 0},
                1: {"name": "BOLD", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "SemanticItalic",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NORMAL", "type": 0, "array": False, "value": 0},
                1: {"name": "ITALIC", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "OpenTypeFeature",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "PCAP", "type": 0, "array": False, "value": 0},
                1: {"name": "C2PC", "type": 0, "array": False, "value": 1},
                2: {"name": "CASE", "type": 0, "array": False, "value": 2},
                3: {"name": "CPSP", "type": 0, "array": False, "value": 3},
                4: {"name": "TITL", "type": 0, "array": False, "value": 4},
                5: {"name": "UNIC", "type": 0, "array": False, "value": 5},
                6: {"name": "ZERO", "type": 0, "array": False, "value": 6},
                7: {"name": "SINF", "type": 0, "array": False, "value": 7},
                8: {"name": "ORDN", "type": 0, "array": False, "value": 8},
                9: {"name": "AFRC", "type": 0, "array": False, "value": 9},
                10: {"name": "DNOM", "type": 0, "array": False, "value": 10},
                11: {"name": "NUMR", "type": 0, "array": False, "value": 11},
                12: {"name": "LIGA", "type": 0, "array": False, "value": 12},
                13: {"name": "CLIG", "type": 0, "array": False, "value": 13},
                14: {"name": "DLIG", "type": 0, "array": False, "value": 14},
                15: {"name": "HLIG", "type": 0, "array": False, "value": 15},
                16: {"name": "RLIG", "type": 0, "array": False, "value": 16},
                17: {"name": "AALT", "type": 0, "array": False, "value": 17},
                18: {"name": "CALT", "type": 0, "array": False, "value": 18},
                19: {"name": "RCLT", "type": 0, "array": False, "value": 19},
                20: {"name": "SALT", "type": 0, "array": False, "value": 20},
                21: {"name": "RVRN", "type": 0, "array": False, "value": 21},
                22: {"name": "VERT", "type": 0, "array": False, "value": 22},
                23: {"name": "SWSH", "type": 0, "array": False, "value": 23},
                24: {"name": "CSWH", "type": 0, "array": False, "value": 24},
                25: {"name": "NALT", "type": 0, "array": False, "value": 25},
                26: {"name": "CCMP", "type": 0, "array": False, "value": 26},
                27: {"name": "STCH", "type": 0, "array": False, "value": 27},
                28: {"name": "HIST", "type": 0, "array": False, "value": 28},
                29: {"name": "SIZE", "type": 0, "array": False, "value": 29},
                30: {"name": "ORNM", "type": 0, "array": False, "value": 30},
                31: {"name": "ITAL", "type": 0, "array": False, "value": 31},
                32: {"name": "RAND", "type": 0, "array": False, "value": 32},
                33: {"name": "DTLS", "type": 0, "array": False, "value": 33},
                34: {"name": "FLAC", "type": 0, "array": False, "value": 34},
                35: {"name": "MGRK", "type": 0, "array": False, "value": 35},
                36: {"name": "SSTY", "type": 0, "array": False, "value": 36},
                37: {"name": "KERN", "type": 0, "array": False, "value": 37},
                38: {"name": "FWID", "type": 0, "array": False, "value": 38},
                39: {"name": "HWID", "type": 0, "array": False, "value": 39},
                40: {"name": "HALT", "type": 0, "array": False, "value": 40},
                41: {"name": "TWID", "type": 0, "array": False, "value": 41},
                42: {"name": "QWID", "type": 0, "array": False, "value": 42},
                43: {"name": "PWID", "type": 0, "array": False, "value": 43},
                44: {"name": "JUST", "type": 0, "array": False, "value": 44},
                45: {"name": "LFBD", "type": 0, "array": False, "value": 45},
                46: {"name": "OPBD", "type": 0, "array": False, "value": 46},
                47: {"name": "RTBD", "type": 0, "array": False, "value": 47},
                48: {"name": "PALT", "type": 0, "array": False, "value": 48},
                49: {"name": "PKNA", "type": 0, "array": False, "value": 49},
                50: {"name": "LTRA", "type": 0, "array": False, "value": 50},
                51: {"name": "LTRM", "type": 0, "array": False, "value": 51},
                52: {"name": "RTLA", "type": 0, "array": False, "value": 52},
                53: {"name": "RTLM", "type": 0, "array": False, "value": 53},
                54: {"name": "ABRV", "type": 0, "array": False, "value": 54},
                55: {"name": "ABVM", "type": 0, "array": False, "value": 55},
                56: {"name": "ABVS", "type": 0, "array": False, "value": 56},
                57: {"name": "VALT", "type": 0, "array": False, "value": 57},
                58: {"name": "VHAL", "type": 0, "array": False, "value": 58},
                59: {"name": "BLWF", "type": 0, "array": False, "value": 59},
                60: {"name": "BLWM", "type": 0, "array": False, "value": 60},
                61: {"name": "BLWS", "type": 0, "array": False, "value": 61},
                62: {"name": "AKHN", "type": 0, "array": False, "value": 62},
                63: {"name": "CJCT", "type": 0, "array": False, "value": 63},
                64: {"name": "CFAR", "type": 0, "array": False, "value": 64},
                65: {"name": "CPCT", "type": 0, "array": False, "value": 65},
                66: {"name": "CURS", "type": 0, "array": False, "value": 66},
                67: {"name": "DIST", "type": 0, "array": False, "value": 67},
                68: {"name": "EXPT", "type": 0, "array": False, "value": 68},
                69: {"name": "FALT", "type": 0, "array": False, "value": 69},
                70: {"name": "FINA", "type": 0, "array": False, "value": 70},
                71: {"name": "FIN2", "type": 0, "array": False, "value": 71},
                72: {"name": "FIN3", "type": 0, "array": False, "value": 72},
                73: {"name": "HALF", "type": 0, "array": False, "value": 73},
                74: {"name": "HALN", "type": 0, "array": False, "value": 74},
                75: {"name": "HKNA", "type": 0, "array": False, "value": 75},
                76: {"name": "HNGL", "type": 0, "array": False, "value": 76},
                77: {"name": "HOJO", "type": 0, "array": False, "value": 77},
                78: {"name": "INIT", "type": 0, "array": False, "value": 78},
                79: {"name": "ISOL", "type": 0, "array": False, "value": 79},
                80: {"name": "JP78", "type": 0, "array": False, "value": 80},
                81: {"name": "JP83", "type": 0, "array": False, "value": 81},
                82: {"name": "JP90", "type": 0, "array": False, "value": 82},
                83: {"name": "JP04", "type": 0, "array": False, "value": 83},
                84: {"name": "LJMO", "type": 0, "array": False, "value": 84},
                85: {"name": "LOCL", "type": 0, "array": False, "value": 85},
                86: {"name": "MARK", "type": 0, "array": False, "value": 86},
                87: {"name": "MEDI", "type": 0, "array": False, "value": 87},
                88: {"name": "MED2", "type": 0, "array": False, "value": 88},
                89: {"name": "MKMK", "type": 0, "array": False, "value": 89},
                90: {"name": "NLCK", "type": 0, "array": False, "value": 90},
                91: {"name": "NUKT", "type": 0, "array": False, "value": 91},
                92: {"name": "PREF", "type": 0, "array": False, "value": 92},
                93: {"name": "PRES", "type": 0, "array": False, "value": 93},
                94: {"name": "VPAL", "type": 0, "array": False, "value": 94},
                95: {"name": "PSTF", "type": 0, "array": False, "value": 95},
                96: {"name": "PSTS", "type": 0, "array": False, "value": 96},
                97: {"name": "RKRF", "type": 0, "array": False, "value": 97},
                98: {"name": "RPHF", "type": 0, "array": False, "value": 98},
                99: {"name": "RUBY", "type": 0, "array": False, "value": 99},
                100: {"name": "SMPL", "type": 0, "array": False, "value": 100},
                101: {"name": "TJMO", "type": 0, "array": False, "value": 101},
                102: {"name": "TNAM", "type": 0, "array": False, "value": 102},
                103: {"name": "TRAD", "type": 0, "array": False, "value": 103},
                104: {"name": "VATU", "type": 0, "array": False, "value": 104},
                105: {"name": "VJMO", "type": 0, "array": False, "value": 105},
                106: {"name": "VKNA", "type": 0, "array": False, "value": 106},
                107: {"name": "VKRN", "type": 0, "array": False, "value": 107},
                108: {"name": "VRTR", "type": 0, "array": False, "value": 108},
                109: {"name": "VRT2", "type": 0, "array": False, "value": 109},
                110: {"name": "SS01", "type": 0, "array": False, "value": 110},
                111: {"name": "SS02", "type": 0, "array": False, "value": 111},
                112: {"name": "SS03", "type": 0, "array": False, "value": 112},
                113: {"name": "SS04", "type": 0, "array": False, "value": 113},
                114: {"name": "SS05", "type": 0, "array": False, "value": 114},
                115: {"name": "SS06", "type": 0, "array": False, "value": 115},
                116: {"name": "SS07", "type": 0, "array": False, "value": 116},
                117: {"name": "SS08", "type": 0, "array": False, "value": 117},
                118: {"name": "SS09", "type": 0, "array": False, "value": 118},
                119: {"name": "SS10", "type": 0, "array": False, "value": 119},
                120: {"name": "SS11", "type": 0, "array": False, "value": 120},
                121: {"name": "SS12", "type": 0, "array": False, "value": 121},
                122: {"name": "SS13", "type": 0, "array": False, "value": 122},
                123: {"name": "SS14", "type": 0, "array": False, "value": 123},
                124: {"name": "SS15", "type": 0, "array": False, "value": 124},
                125: {"name": "SS16", "type": 0, "array": False, "value": 125},
                126: {"name": "SS17", "type": 0, "array": False, "value": 126},
                127: {"name": "SS18", "type": 0, "array": False, "value": 127},
                128: {"name": "SS19", "type": 0, "array": False, "value": 128},
                129: {"name": "SS20", "type": 0, "array": False, "value": 129},
                130: {"name": "CV01", "type": 0, "array": False, "value": 130},
                131: {"name": "CV02", "type": 0, "array": False, "value": 131},
                132: {"name": "CV03", "type": 0, "array": False, "value": 132},
                133: {"name": "CV04", "type": 0, "array": False, "value": 133},
                134: {"name": "CV05", "type": 0, "array": False, "value": 134},
                135: {"name": "CV06", "type": 0, "array": False, "value": 135},
                136: {"name": "CV07", "type": 0, "array": False, "value": 136},
                137: {"name": "CV08", "type": 0, "array": False, "value": 137},
                138: {"name": "CV09", "type": 0, "array": False, "value": 138},
                139: {"name": "CV10", "type": 0, "array": False, "value": 139},
                140: {"name": "CV11", "type": 0, "array": False, "value": 140},
                141: {"name": "CV12", "type": 0, "array": False, "value": 141},
                142: {"name": "CV13", "type": 0, "array": False, "value": 142},
                143: {"name": "CV14", "type": 0, "array": False, "value": 143},
                144: {"name": "CV15", "type": 0, "array": False, "value": 144},
                145: {"name": "CV16", "type": 0, "array": False, "value": 145},
                146: {"name": "CV17", "type": 0, "array": False, "value": 146},
                147: {"name": "CV18", "type": 0, "array": False, "value": 147},
                148: {"name": "CV19", "type": 0, "array": False, "value": 148},
                149: {"name": "CV20", "type": 0, "array": False, "value": 149},
                150: {"name": "CV21", "type": 0, "array": False, "value": 150},
                151: {"name": "CV22", "type": 0, "array": False, "value": 151},
                152: {"name": "CV23", "type": 0, "array": False, "value": 152},
                153: {"name": "CV24", "type": 0, "array": False, "value": 153},
                154: {"name": "CV25", "type": 0, "array": False, "value": 154},
                155: {"name": "CV26", "type": 0, "array": False, "value": 155},
                156: {"name": "CV27", "type": 0, "array": False, "value": 156},
                157: {"name": "CV28", "type": 0, "array": False, "value": 157},
                158: {"name": "CV29", "type": 0, "array": False, "value": 158},
                159: {"name": "CV30", "type": 0, "array": False, "value": 159},
                160: {"name": "CV31", "type": 0, "array": False, "value": 160},
                161: {"name": "CV32", "type": 0, "array": False, "value": 161},
                162: {"name": "CV33", "type": 0, "array": False, "value": 162},
                163: {"name": "CV34", "type": 0, "array": False, "value": 163},
                164: {"name": "CV35", "type": 0, "array": False, "value": 164},
                165: {"name": "CV36", "type": 0, "array": False, "value": 165},
                166: {"name": "CV37", "type": 0, "array": False, "value": 166},
                167: {"name": "CV38", "type": 0, "array": False, "value": 167},
                168: {"name": "CV39", "type": 0, "array": False, "value": 168},
                169: {"name": "CV40", "type": 0, "array": False, "value": 169},
                170: {"name": "CV41", "type": 0, "array": False, "value": 170},
                171: {"name": "CV42", "type": 0, "array": False, "value": 171},
                172: {"name": "CV43", "type": 0, "array": False, "value": 172},
                173: {"name": "CV44", "type": 0, "array": False, "value": 173},
                174: {"name": "CV45", "type": 0, "array": False, "value": 174},
                175: {"name": "CV46", "type": 0, "array": False, "value": 175},
                176: {"name": "CV47", "type": 0, "array": False, "value": 176},
                177: {"name": "CV48", "type": 0, "array": False, "value": 177},
                178: {"name": "CV49", "type": 0, "array": False, "value": 178},
                179: {"name": "CV50", "type": 0, "array": False, "value": 179},
                180: {"name": "CV51", "type": 0, "array": False, "value": 180},
                181: {"name": "CV52", "type": 0, "array": False, "value": 181},
                182: {"name": "CV53", "type": 0, "array": False, "value": 182},
                183: {"name": "CV54", "type": 0, "array": False, "value": 183},
                184: {"name": "CV55", "type": 0, "array": False, "value": 184},
                185: {"name": "CV56", "type": 0, "array": False, "value": 185},
                186: {"name": "CV57", "type": 0, "array": False, "value": 186},
                187: {"name": "CV58", "type": 0, "array": False, "value": 187},
                188: {"name": "CV59", "type": 0, "array": False, "value": 188},
                189: {"name": "CV60", "type": 0, "array": False, "value": 189},
                190: {"name": "CV61", "type": 0, "array": False, "value": 190},
                191: {"name": "CV62", "type": 0, "array": False, "value": 191},
                192: {"name": "CV63", "type": 0, "array": False, "value": 192},
                193: {"name": "CV64", "type": 0, "array": False, "value": 193},
                194: {"name": "CV65", "type": 0, "array": False, "value": 194},
                195: {"name": "CV66", "type": 0, "array": False, "value": 195},
                196: {"name": "CV67", "type": 0, "array": False, "value": 196},
                197: {"name": "CV68", "type": 0, "array": False, "value": 197},
                198: {"name": "CV69", "type": 0, "array": False, "value": 198},
                199: {"name": "CV70", "type": 0, "array": False, "value": 199},
                200: {"name": "CV71", "type": 0, "array": False, "value": 200},
                201: {"name": "CV72", "type": 0, "array": False, "value": 201},
                202: {"name": "CV73", "type": 0, "array": False, "value": 202},
                203: {"name": "CV74", "type": 0, "array": False, "value": 203},
                204: {"name": "CV75", "type": 0, "array": False, "value": 204},
                205: {"name": "CV76", "type": 0, "array": False, "value": 205},
                206: {"name": "CV77", "type": 0, "array": False, "value": 206},
                207: {"name": "CV78", "type": 0, "array": False, "value": 207},
                208: {"name": "CV79", "type": 0, "array": False, "value": 208},
                209: {"name": "CV80", "type": 0, "array": False, "value": 209},
                210: {"name": "CV81", "type": 0, "array": False, "value": 210},
                211: {"name": "CV82", "type": 0, "array": False, "value": 211},
                212: {"name": "CV83", "type": 0, "array": False, "value": 212},
                213: {"name": "CV84", "type": 0, "array": False, "value": 213},
                214: {"name": "CV85", "type": 0, "array": False, "value": 214},
                215: {"name": "CV86", "type": 0, "array": False, "value": 215},
                216: {"name": "CV87", "type": 0, "array": False, "value": 216},
                217: {"name": "CV88", "type": 0, "array": False, "value": 217},
                218: {"name": "CV89", "type": 0, "array": False, "value": 218},
                219: {"name": "CV90", "type": 0, "array": False, "value": 219},
                220: {"name": "CV91", "type": 0, "array": False, "value": 220},
                221: {"name": "CV92", "type": 0, "array": False, "value": 221},
                222: {"name": "CV93", "type": 0, "array": False, "value": 222},
                223: {"name": "CV94", "type": 0, "array": False, "value": 223},
                224: {"name": "CV95", "type": 0, "array": False, "value": 224},
                225: {"name": "CV96", "type": 0, "array": False, "value": 225},
                226: {"name": "CV97", "type": 0, "array": False, "value": 226},
                227: {"name": "CV98", "type": 0, "array": False, "value": 227},
                228: {"name": "CV99", "type": 0, "array": False, "value": 228},
            }
        ),
    },
    {
        "name": "ExportConstraint",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "type", "type": 26, "array": False, "value": 1},
                2: {"name": "value", "type": -5, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "GUIDMapping",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "from", "type": 47, "array": False, "value": 1},
                2: {"name": "to", "type": 47, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "Blob",
        "kind": 1,
        "fields": OrderedDict({1: {"name": "bytes", "type": -2, "array": True, "value": 1}}),
    },
    {
        "name": "Image",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "hash", "type": -2, "array": True, "value": 1},
                2: {"name": "name", "type": -6, "array": False, "value": 2},
                3: {"name": "dataBlob", "type": -4, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "Video",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "hash", "type": -2, "array": True, "value": 1},
                2: {"name": "s3Url", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "FilterColorAdjust",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "tint", "type": -5, "array": False, "value": 1},
                2: {"name": "shadows", "type": -5, "array": False, "value": 2},
                3: {"name": "highlights", "type": -5, "array": False, "value": 3},
                4: {"name": "detail", "type": -5, "array": False, "value": 4},
                5: {"name": "exposure", "type": -5, "array": False, "value": 5},
                6: {"name": "vignette", "type": -5, "array": False, "value": 6},
                7: {"name": "temperature", "type": -5, "array": False, "value": 7},
                8: {"name": "vibrance", "type": -5, "array": False, "value": 8},
            }
        ),
    },
    {
        "name": "PaintFilterMessage",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "tint", "type": -5, "array": False, "value": 1},
                2: {"name": "shadows", "type": -5, "array": False, "value": 2},
                3: {"name": "highlights", "type": -5, "array": False, "value": 3},
                4: {"name": "detail", "type": -5, "array": False, "value": 4},
                5: {"name": "exposure", "type": -5, "array": False, "value": 5},
                6: {"name": "vignette", "type": -5, "array": False, "value": 6},
                7: {"name": "temperature", "type": -5, "array": False, "value": 7},
                8: {"name": "vibrance", "type": -5, "array": False, "value": 8},
                9: {"name": "contrast", "type": -5, "array": False, "value": 9},
                10: {"name": "brightness", "type": -5, "array": False, "value": 10},
            }
        ),
    },
    {
        "name": "Paint",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "type", "type": 8, "array": False, "value": 1},
                2: {"name": "color", "type": 48, "array": False, "value": 2},
                3: {"name": "opacity", "type": -5, "array": False, "value": 3},
                4: {"name": "visible", "type": -1, "array": False, "value": 4},
                5: {"name": "blendMode", "type": 7, "array": False, "value": 5},
                6: {"name": "stops", "type": 51, "array": True, "value": 6},
                7: {"name": "transform", "type": 52, "array": False, "value": 7},
                8: {"name": "image", "type": 68, "array": False, "value": 8},
                9: {"name": "imageThumbnail", "type": 68, "array": False, "value": 9},
                16: {"name": "animatedImage", "type": 68, "array": False, "value": 16},
                17: {"name": "animationFrame", "type": -4, "array": False, "value": 17},
                10: {"name": "imageScaleMode", "type": 9, "array": False, "value": 10},
                22: {"name": "imageShouldColorManage", "type": -1, "array": False, "value": 22},
                11: {"name": "rotation", "type": -5, "array": False, "value": 11},
                12: {"name": "scale", "type": -5, "array": False, "value": 12},
                13: {"name": "filterColorAdjust", "type": 70, "array": False, "value": 13},
                14: {"name": "paintFilter", "type": 71, "array": False, "value": 14},
                15: {"name": "emojiCodePoints", "type": -4, "array": True, "value": 15},
                18: {"name": "video", "type": 69, "array": False, "value": 18},
                19: {"name": "originalImageWidth", "type": -4, "array": False, "value": 19},
                20: {"name": "originalImageHeight", "type": -4, "array": False, "value": 20},
                21: {"name": "colorVar", "type": 269, "array": False, "value": 21},
            }
        ),
    },
    {
        "name": "FontMetaData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "key", "type": 55, "array": False, "value": 1},
                2: {"name": "fontLineHeight", "type": -5, "array": False, "value": 2},
                3: {"name": "fontDigest", "type": -2, "array": True, "value": 3},
                4: {"name": "fontStyle", "type": 61, "array": False, "value": 4},
                5: {"name": "fontWeight", "type": -3, "array": False, "value": 5},
            }
        ),
    },
    {
        "name": "FontVariation",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "axisTag", "type": -4, "array": False, "value": 1},
                2: {"name": "axisName", "type": -6, "array": False, "value": 2},
                3: {"name": "value", "type": -5, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "TextData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "characters", "type": -6, "array": False, "value": 1},
                2: {"name": "characterStyleIDs", "type": -4, "array": True, "value": 2},
                3: {"name": "styleOverrideTable", "type": 152, "array": True, "value": 3},
                4: {"name": "layoutSize", "type": 49, "array": False, "value": 4},
                5: {"name": "baselines", "type": 79, "array": True, "value": 5},
                6: {"name": "glyphs", "type": 80, "array": True, "value": 6},
                7: {"name": "decorations", "type": 81, "array": True, "value": 7},
                16: {"name": "blockquotes", "type": 82, "array": True, "value": 16},
                8: {"name": "layoutVersion", "type": -4, "array": False, "value": 8},
                9: {"name": "fontMetaData", "type": 73, "array": True, "value": 9},
                10: {"name": "fallbackFonts", "type": 55, "array": True, "value": 10},
                11: {"name": "hyperlinkBoxes", "type": 77, "array": True, "value": 11},
                12: {"name": "lines", "type": 203, "array": True, "value": 12},
                13: {"name": "truncationStartIndex", "type": -3, "array": False, "value": 13},
                14: {"name": "truncatedHeight", "type": -5, "array": False, "value": 14},
                15: {
                    "name": "logicalIndexToCharacterOffsetMap",
                    "type": -5,
                    "array": True,
                    "value": 15,
                },
                17: {"name": "minContentHeight", "type": -5, "array": False, "value": 17},
                18: {"name": "mentionBoxes", "type": 78, "array": True, "value": 18},
                19: {"name": "derivedLines", "type": 204, "array": True, "value": 19},
            }
        ),
    },
    {
        "name": "DerivedTextData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "layoutSize", "type": 49, "array": False, "value": 1},
                2: {"name": "baselines", "type": 79, "array": True, "value": 2},
                3: {"name": "glyphs", "type": 80, "array": True, "value": 3},
                4: {"name": "decorations", "type": 81, "array": True, "value": 4},
                5: {"name": "blockquotes", "type": 82, "array": True, "value": 5},
                6: {"name": "fontMetaData", "type": 73, "array": True, "value": 6},
                7: {"name": "hyperlinkBoxes", "type": 77, "array": True, "value": 7},
                8: {"name": "truncationStartIndex", "type": -3, "array": False, "value": 8},
                9: {"name": "truncatedHeight", "type": -5, "array": False, "value": 9},
                10: {
                    "name": "logicalIndexToCharacterOffsetMap",
                    "type": -5,
                    "array": True,
                    "value": 10,
                },
                11: {"name": "mentionBoxes", "type": 78, "array": True, "value": 11},
                12: {"name": "derivedLines", "type": 204, "array": True, "value": 12},
            }
        ),
    },
    {
        "name": "HyperlinkBox",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "bounds", "type": 50, "array": False, "value": 1},
                2: {"name": "url", "type": -6, "array": False, "value": 2},
                3: {"name": "guid", "type": 47, "array": False, "value": 3},
                4: {"name": "hyperlinkID", "type": -3, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "MentionBox",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "bounds", "type": 50, "array": False, "value": 1},
                2: {"name": "startIndex", "type": -4, "array": False, "value": 2},
                3: {"name": "endIndex", "type": -4, "array": False, "value": 3},
                4: {"name": "isValid", "type": -1, "array": False, "value": 4},
                5: {"name": "mentionKey", "type": -4, "array": False, "value": 5},
            }
        ),
    },
    {
        "name": "Baseline",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "position", "type": 49, "array": False, "value": 1},
                2: {"name": "width", "type": -5, "array": False, "value": 2},
                3: {"name": "lineY", "type": -5, "array": False, "value": 3},
                4: {"name": "lineHeight", "type": -5, "array": False, "value": 4},
                7: {"name": "lineAscent", "type": -5, "array": False, "value": 7},
                8: {"name": "ignoreLeadingTrim", "type": -5, "array": False, "value": 8},
                5: {"name": "firstCharacter", "type": -4, "array": False, "value": 5},
                6: {"name": "endCharacter", "type": -4, "array": False, "value": 6},
            }
        ),
    },
    {
        "name": "Glyph",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "commandsBlob", "type": -4, "array": False, "value": 1},
                2: {"name": "position", "type": 49, "array": False, "value": 2},
                3: {"name": "styleID", "type": -4, "array": False, "value": 3},
                4: {"name": "fontSize", "type": -5, "array": False, "value": 4},
                5: {"name": "firstCharacter", "type": -4, "array": False, "value": 5},
                6: {"name": "advance", "type": -5, "array": False, "value": 6},
                7: {"name": "emojiCodePoints", "type": -4, "array": True, "value": 7},
            }
        ),
    },
    {
        "name": "Decoration",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "rects", "type": 50, "array": True, "value": 1},
                2: {"name": "styleID", "type": -4, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "Blockquote",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "verticalBar", "type": 50, "array": False, "value": 1},
                2: {"name": "quoteMarkBounds", "type": 50, "array": False, "value": 2},
                3: {"name": "styleID", "type": -4, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "VectorData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "vectorNetworkBlob", "type": -4, "array": False, "value": 1},
                2: {"name": "normalizedSize", "type": 49, "array": False, "value": 2},
                3: {"name": "styleOverrideTable", "type": 152, "array": True, "value": 3},
            }
        ),
    },
    {
        "name": "GUIDPath",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "guids", "type": 47, "array": True, "value": 1}}),
    },
    {
        "name": "SymbolData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "symbolID", "type": 47, "array": False, "value": 1},
                2: {"name": "symbolOverrides", "type": 152, "array": True, "value": 2},
                3: {"name": "uniformScaleFactor", "type": -5, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "GUIDPathMapping",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "id", "type": 47, "array": False, "value": 1},
                2: {"name": "path", "type": 84, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "NodeGenerationData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "overrides", "type": 152, "array": True, "value": 1},
                2: {"name": "useFineGrainedSyncing", "type": -1, "array": False, "value": 2},
                3: {"name": "diffOnlyRemovals", "type": 152, "array": True, "value": 3},
            }
        ),
    },
    {
        "name": "DerivedImmutableFrameData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "overrides", "type": 152, "array": True, "value": 1},
                2: {"name": "version", "type": -4, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "AssetIdMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 90, "array": True, "value": 1}}),
    },
    {
        "name": "AssetIdEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "assetKey", "type": -6, "array": False, "value": 1},
                2: {"name": "assetId", "type": 92, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "AssetRef",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "key", "type": -6, "array": False, "value": 1},
                2: {"name": "version", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "AssetId",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                2: {"name": "assetRef", "type": 91, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "StateGroupId",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                2: {"name": "assetRef", "type": 91, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "StyleId",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                2: {"name": "assetRef", "type": 91, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "SymbolId",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                2: {"name": "assetRef", "type": 91, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "VariableID",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                2: {"name": "assetRef", "type": 91, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "VariableOverrideId",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                2: {"name": "assetRef", "type": 91, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "VariableSetID",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                2: {"name": "assetRef", "type": 91, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ThemeID",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                2: {"name": "assetRef", "type": 91, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "SlideThemeData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "themeID", "type": 99, "array": False, "value": 1},
                2: {"name": "version", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "SharedSymbolReference",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "fileKey", "type": -6, "array": False, "value": 1},
                2: {"name": "symbolID", "type": 47, "array": False, "value": 2},
                3: {"name": "versionHash", "type": -6, "array": False, "value": 3},
                4: {"name": "guidPathMappings", "type": 86, "array": True, "value": 4},
                5: {"name": "bytes", "type": -2, "array": True, "value": 5},
                6: {"name": "libraryGUIDToSubscribingGUID", "type": 66, "array": True, "value": 6},
                7: {"name": "componentKey", "type": -6, "array": False, "value": 7},
                8: {"name": "unflatteningMappings", "type": 86, "array": True, "value": 8},
                9: {"name": "isUnflattened", "type": -1, "array": False, "value": 9},
            }
        ),
    },
    {
        "name": "SharedComponentMasterData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "componentKey", "type": -6, "array": False, "value": 1},
                2: {
                    "name": "publishingGUIDPathToTeamLibraryGUID",
                    "type": 86,
                    "array": True,
                    "value": 2,
                },
                3: {"name": "isUnflattened", "type": -1, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "InstanceOverrideStash",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {
                    "name": "overridePathOfSwappedInstance",
                    "type": 84,
                    "array": False,
                    "value": 1,
                },
                2: {"name": "componentKey", "type": -6, "array": False, "value": 2},
                3: {"name": "overrides", "type": 152, "array": True, "value": 3},
            }
        ),
    },
    {
        "name": "InstanceOverrideStashV2",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {
                    "name": "overridePathOfSwappedInstance",
                    "type": 84,
                    "array": False,
                    "value": 1,
                },
                2: {"name": "localSymbolID", "type": 47, "array": False, "value": 2},
                3: {"name": "overrides", "type": 152, "array": True, "value": 3},
            }
        ),
    },
    {
        "name": "Effect",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "type", "type": 10, "array": False, "value": 1},
                2: {"name": "color", "type": 48, "array": False, "value": 2},
                3: {"name": "offset", "type": 49, "array": False, "value": 3},
                4: {"name": "radius", "type": -5, "array": False, "value": 4},
                5: {"name": "visible", "type": -1, "array": False, "value": 5},
                6: {"name": "blendMode", "type": 7, "array": False, "value": 6},
                7: {"name": "spread", "type": -5, "array": False, "value": 7},
                8: {"name": "showShadowBehindNode", "type": -1, "array": False, "value": 8},
                9: {"name": "radiusVar", "type": 269, "array": False, "value": 9},
                10: {"name": "colorVar", "type": 269, "array": False, "value": 10},
                11: {"name": "spreadVar", "type": 269, "array": False, "value": 11},
                12: {"name": "xVar", "type": 269, "array": False, "value": 12},
                13: {"name": "yVar", "type": 269, "array": False, "value": 13},
            }
        ),
    },
    {
        "name": "TransitionInfo",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "type", "type": 43, "array": False, "value": 1},
                2: {"name": "duration", "type": -5, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "PrototypeDeviceType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "PRESET", "type": 0, "array": False, "value": 1},
                2: {"name": "CUSTOM", "type": 0, "array": False, "value": 2},
                3: {"name": "PRESENTATION", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "DeviceRotation",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "CCW_90", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "PrototypeDevice",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "type", "type": 107, "array": False, "value": 1},
                2: {"name": "size", "type": 49, "array": False, "value": 2},
                3: {"name": "presetIdentifier", "type": -6, "array": False, "value": 3},
                4: {"name": "rotation", "type": 108, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "OverlayPositionType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "CENTER", "type": 0, "array": False, "value": 0},
                1: {"name": "TOP_LEFT", "type": 0, "array": False, "value": 1},
                2: {"name": "TOP_CENTER", "type": 0, "array": False, "value": 2},
                3: {"name": "TOP_RIGHT", "type": 0, "array": False, "value": 3},
                4: {"name": "BOTTOM_LEFT", "type": 0, "array": False, "value": 4},
                5: {"name": "BOTTOM_CENTER", "type": 0, "array": False, "value": 5},
                6: {"name": "BOTTOM_RIGHT", "type": 0, "array": False, "value": 6},
                7: {"name": "MANUAL", "type": 0, "array": False, "value": 7},
            }
        ),
    },
    {
        "name": "OverlayBackgroundInteraction",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "CLOSE_ON_CLICK_OUTSIDE", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "OverlayBackgroundType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "SOLID_COLOR", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "OverlayBackgroundAppearance",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "backgroundType", "type": 112, "array": False, "value": 1},
                2: {"name": "backgroundColor", "type": 48, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "NavigationType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NAVIGATE", "type": 0, "array": False, "value": 0},
                1: {"name": "OVERLAY", "type": 0, "array": False, "value": 1},
                2: {"name": "SWAP", "type": 0, "array": False, "value": 2},
                3: {"name": "SWAP_STATE", "type": 0, "array": False, "value": 3},
                4: {"name": "SCROLL_TO", "type": 0, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "ExportColorProfile",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "DOCUMENT", "type": 0, "array": False, "value": 0},
                1: {"name": "SRGB", "type": 0, "array": False, "value": 1},
                2: {"name": "DISPLAY_P3_V4", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ExportSettings",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "suffix", "type": -6, "array": False, "value": 1},
                2: {"name": "imageType", "type": 25, "array": False, "value": 2},
                3: {"name": "constraint", "type": 65, "array": False, "value": 3},
                4: {"name": "svgDataName", "type": -1, "array": False, "value": 4},
                5: {"name": "svgIDMode", "type": 117, "array": False, "value": 5},
                6: {"name": "svgOutlineText", "type": -1, "array": False, "value": 6},
                7: {"name": "contentsOnly", "type": -1, "array": False, "value": 7},
                8: {"name": "svgForceStrokeMasks", "type": -1, "array": False, "value": 8},
                9: {"name": "useAbsoluteBounds", "type": -1, "array": False, "value": 9},
                10: {"name": "colorProfile", "type": 115, "array": False, "value": 10},
            }
        ),
    },
    {
        "name": "ExportSVGIDMode",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "IF_NEEDED", "type": 0, "array": False, "value": 0},
                1: {"name": "ALWAYS", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "LayoutGrid",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "type", "type": 27, "array": False, "value": 1},
                2: {"name": "axis", "type": 1, "array": False, "value": 2},
                3: {"name": "visible", "type": -1, "array": False, "value": 3},
                4: {"name": "numSections", "type": -3, "array": False, "value": 4},
                5: {"name": "offset", "type": -5, "array": False, "value": 5},
                6: {"name": "sectionSize", "type": -5, "array": False, "value": 6},
                7: {"name": "gutterSize", "type": -5, "array": False, "value": 7},
                8: {"name": "color", "type": 48, "array": False, "value": 8},
                9: {"name": "pattern", "type": 28, "array": False, "value": 9},
                10: {"name": "numSectionsVar", "type": 269, "array": False, "value": 10},
                11: {"name": "offsetVar", "type": 269, "array": False, "value": 11},
                12: {"name": "sectionSizeVar", "type": 269, "array": False, "value": 12},
                13: {"name": "gutterSizeVar", "type": 269, "array": False, "value": 13},
            }
        ),
    },
    {
        "name": "Guide",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "axis", "type": 1, "array": False, "value": 1},
                2: {"name": "offset", "type": -5, "array": False, "value": 2},
                3: {"name": "guid", "type": 47, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "Path",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "windingRule", "type": 4, "array": False, "value": 1},
                2: {"name": "commandsBlob", "type": -4, "array": False, "value": 2},
                3: {"name": "styleID", "type": -4, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "StyleType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "FILL", "type": 0, "array": False, "value": 1},
                2: {"name": "STROKE", "type": 0, "array": False, "value": 2},
                3: {"name": "TEXT", "type": 0, "array": False, "value": 3},
                4: {"name": "EFFECT", "type": 0, "array": False, "value": 4},
                5: {"name": "EXPORT", "type": 0, "array": False, "value": 5},
                6: {"name": "GRID", "type": 0, "array": False, "value": 6},
            }
        ),
    },
    {
        "name": "SharedStyleReference",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "styleKey", "type": -6, "array": False, "value": 1},
                2: {"name": "versionHash", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "SharedStyleMasterData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "styleKey", "type": -6, "array": False, "value": 1},
                2: {"name": "sortPosition", "type": -6, "array": False, "value": 2},
                3: {"name": "fileKey", "type": -6, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "ScrollBehavior",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "SCROLLS", "type": 0, "array": False, "value": 0},
                1: {
                    "name": "FIXED_WHEN_CHILD_OF_SCROLLING_FRAME",
                    "type": 0,
                    "array": False,
                    "value": 1,
                },
                2: {"name": "STICKY_SCROLLS", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ArcData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "startingAngle", "type": -5, "array": False, "value": 1},
                2: {"name": "endingAngle", "type": -5, "array": False, "value": 2},
                3: {"name": "innerRadius", "type": -5, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "SymbolLink",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "uri", "type": -6, "array": False, "value": 1},
                2: {"name": "displayName", "type": -6, "array": False, "value": 2},
                3: {"name": "displayText", "type": -6, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "PluginData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "pluginID", "type": -6, "array": False, "value": 1},
                2: {"name": "value", "type": -6, "array": False, "value": 2},
                3: {"name": "key", "type": -6, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "PluginRelaunchData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "pluginID", "type": -6, "array": False, "value": 1},
                2: {"name": "message", "type": -6, "array": False, "value": 2},
                3: {"name": "command", "type": -6, "array": False, "value": 3},
                4: {"name": "isDeleted", "type": -1, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "MultiplayerFieldVersion",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "counter", "type": -4, "array": False, "value": 1},
                2: {"name": "sessionID", "type": -4, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ConnectorMagnet",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "AUTO", "type": 0, "array": False, "value": 1},
                2: {"name": "TOP", "type": 0, "array": False, "value": 2},
                3: {"name": "LEFT", "type": 0, "array": False, "value": 3},
                4: {"name": "BOTTOM", "type": 0, "array": False, "value": 4},
                5: {"name": "RIGHT", "type": 0, "array": False, "value": 5},
                6: {"name": "CENTER", "type": 0, "array": False, "value": 6},
                7: {"name": "AUTO_HORIZONTAL", "type": 0, "array": False, "value": 7},
            }
        ),
    },
    {
        "name": "ConnectorEndpoint",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "endpointNodeID", "type": 47, "array": False, "value": 1},
                2: {"name": "position", "type": 49, "array": False, "value": 2},
                3: {"name": "magnet", "type": 130, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "ConnectorControlPoint",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "position", "type": 49, "array": False, "value": 1},
                2: {"name": "axis", "type": 49, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ConnectorTextSection",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "MIDDLE_TO_START", "type": 0, "array": False, "value": 0},
                1: {"name": "MIDDLE_TO_END", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "ConnectorTextMidpoint",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "section", "type": 133, "array": False, "value": 1},
                2: {"name": "offset", "type": -5, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ConnectorLineStyle",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "ELBOWED", "type": 0, "array": False, "value": 0},
                1: {"name": "STRAIGHT", "type": 0, "array": False, "value": 1},
                2: {"name": "CURVED", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ConnectorType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "MANUAL", "type": 0, "array": False, "value": 0},
                1: {"name": "DIAGRAM", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "AnnotationPropertyType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "FILL", "type": 0, "array": False, "value": 0},
                1: {"name": "STROKE", "type": 0, "array": False, "value": 1},
                2: {"name": "WIDTH", "type": 0, "array": False, "value": 2},
                3: {"name": "HEIGHT", "type": 0, "array": False, "value": 3},
                4: {"name": "MIN_WIDTH", "type": 0, "array": False, "value": 4},
                5: {"name": "MIN_HEIGHT", "type": 0, "array": False, "value": 5},
                6: {"name": "MAX_WIDTH", "type": 0, "array": False, "value": 6},
                7: {"name": "MAX_HEIGHT", "type": 0, "array": False, "value": 7},
                8: {"name": "STROKE_WIDTH", "type": 0, "array": False, "value": 8},
                9: {"name": "CORNER_RADIUS", "type": 0, "array": False, "value": 9},
                10: {"name": "EFFECT", "type": 0, "array": False, "value": 10},
                11: {"name": "TEXT_STYLE", "type": 0, "array": False, "value": 11},
                12: {"name": "TEXT_ALIGN_HORIZONTAL", "type": 0, "array": False, "value": 12},
                13: {"name": "FONT_FAMILY", "type": 0, "array": False, "value": 13},
                14: {"name": "FONT_SIZE", "type": 0, "array": False, "value": 14},
                15: {"name": "FONT_WEIGHT", "type": 0, "array": False, "value": 15},
                16: {"name": "LINE_HEIGHT", "type": 0, "array": False, "value": 16},
                17: {"name": "LETTER_SPACING", "type": 0, "array": False, "value": 17},
                18: {"name": "STACK_SPACING", "type": 0, "array": False, "value": 18},
                19: {"name": "STACK_PADDING", "type": 0, "array": False, "value": 19},
                20: {"name": "STACK_MODE", "type": 0, "array": False, "value": 20},
                21: {"name": "STACK_ALIGNMENT", "type": 0, "array": False, "value": 21},
                22: {"name": "OPACITY", "type": 0, "array": False, "value": 22},
            }
        ),
    },
    {
        "name": "AnnotationProperty",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "type", "type": 137, "array": False, "value": 1}}),
    },
    {
        "name": "Annotation",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "label", "type": -6, "array": False, "value": 1},
                2: {"name": "properties", "type": 138, "array": True, "value": 2},
            }
        ),
    },
    {
        "name": "AnnotationMeasurementNodeSide",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "TOP", "type": 0, "array": False, "value": 0},
                1: {"name": "BOTTOM", "type": 0, "array": False, "value": 1},
                2: {"name": "LEFT", "type": 0, "array": False, "value": 2},
                3: {"name": "RIGHT", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "AnnotationMeasurement",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "id", "type": 47, "array": False, "value": 1},
                2: {"name": "fromNode", "type": 47, "array": False, "value": 2},
                3: {"name": "toNode", "type": 47, "array": False, "value": 3},
                4: {"name": "fromNodeSide", "type": 140, "array": False, "value": 4},
                5: {"name": "toSameSide", "type": -1, "array": False, "value": 5},
                6: {"name": "innerOffsetRelative", "type": -5, "array": False, "value": 6},
                7: {"name": "outerOffsetFixed", "type": -5, "array": False, "value": 7},
            }
        ),
    },
    {
        "name": "LibraryMoveInfo",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "oldKey", "type": -6, "array": False, "value": 1},
                2: {"name": "pasteFileKey", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "LibraryMoveHistoryItem",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "sourceNodeId", "type": 47, "array": False, "value": 1},
                2: {"name": "sourceComponentKey", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "DeveloperRelatedLink",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "nodeId", "type": -6, "array": False, "value": 1},
                2: {"name": "fileKey", "type": -6, "array": False, "value": 2},
                3: {"name": "linkName", "type": -6, "array": False, "value": 3},
                4: {"name": "linkUrl", "type": -6, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "WidgetPointer",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "nodeId", "type": 47, "array": False, "value": 1}}),
    },
    {
        "name": "EditInfo",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "timestampIso8601", "type": -6, "array": False, "value": 1},
                2: {"name": "userId", "type": -6, "array": False, "value": 2},
                3: {"name": "lastEditedAt", "type": -4, "array": False, "value": 3},
                4: {"name": "createdAt", "type": -4, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "EditorType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "DESIGN", "type": 0, "array": False, "value": 0},
                1: {"name": "WHITEBOARD", "type": 0, "array": False, "value": 1},
                2: {"name": "SLIDES", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "MaskType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "ALPHA", "type": 0, "array": False, "value": 0},
                1: {"name": "OUTLINE", "type": 0, "array": False, "value": 1},
                2: {"name": "LUMINANCE", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ModuleType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "SINGLE_NODE", "type": 0, "array": False, "value": 1},
                2: {"name": "MULTI_NODE", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "SectionStatus",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "BUILD", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "SectionStatusInfo",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "status", "type": 150, "array": False, "value": 1}}),
    },
    {
        "name": "NodeChange",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                53: {"name": "guidTag", "type": -4, "array": False, "value": 53},
                2: {"name": "phase", "type": 3, "array": False, "value": 2},
                54: {"name": "phaseTag", "type": -4, "array": False, "value": 54},
                3: {"name": "parentIndex", "type": 53, "array": False, "value": 3},
                55: {"name": "parentIndexTag", "type": -4, "array": False, "value": 55},
                4: {"name": "type", "type": 5, "array": False, "value": 4},
                56: {"name": "typeTag", "type": -4, "array": False, "value": 56},
                5: {"name": "name", "type": -6, "array": False, "value": 5},
                57: {"name": "nameTag", "type": -4, "array": False, "value": 57},
                174: {"name": "isPublishable", "type": -1, "array": False, "value": 174},
                318: {"name": "description", "type": -6, "array": False, "value": 318},
                256: {"name": "libraryMoveInfo", "type": 142, "array": False, "value": 256},
                281: {"name": "libraryMoveHistory", "type": 143, "array": True, "value": 281},
                319: {"name": "key", "type": -6, "array": False, "value": 319},
                383: {"name": "fileAssetIds", "type": 89, "array": False, "value": 383},
                49: {"name": "styleID", "type": -4, "array": False, "value": 49},
                101: {"name": "styleIDTag", "type": -4, "array": False, "value": 101},
                176: {"name": "isSoftDeletedStyle", "type": -1, "array": False, "value": 176},
                177: {"name": "isNonUpdateable", "type": -1, "array": False, "value": 177},
                157: {"name": "isFillStyle", "type": -1, "array": False, "value": 157},
                161: {"name": "isStrokeStyle", "type": -1, "array": False, "value": 161},
                376: {"name": "isOverrideOverTextStyle", "type": -1, "array": False, "value": 376},
                163: {"name": "styleType", "type": 121, "array": False, "value": 163},
                191: {"name": "styleDescription", "type": -6, "array": False, "value": 191},
                171: {"name": "version", "type": -6, "array": False, "value": 171},
                172: {"name": "sharedStyleMasterData", "type": 123, "array": False, "value": 172},
                173: {"name": "sharedStyleReference", "type": 122, "array": False, "value": 173},
                320: {"name": "sortPosition", "type": -6, "array": False, "value": 320},
                345: {
                    "name": "ojansSuperSecretNodeField",
                    "type": 123,
                    "array": False,
                    "value": 345,
                },
                348: {"name": "sevMoonlitLilyData", "type": 123, "array": False, "value": 348},
                158: {"name": "inheritFillStyleID", "type": 47, "array": False, "value": 158},
                162: {"name": "inheritStrokeStyleID", "type": 47, "array": False, "value": 162},
                167: {"name": "inheritTextStyleID", "type": 47, "array": False, "value": 167},
                168: {"name": "inheritExportStyleID", "type": 47, "array": False, "value": 168},
                169: {"name": "inheritEffectStyleID", "type": 47, "array": False, "value": 169},
                170: {"name": "inheritGridStyleID", "type": 47, "array": False, "value": 170},
                185: {
                    "name": "inheritFillStyleIDForStroke",
                    "type": 47,
                    "array": False,
                    "value": 185,
                },
                332: {"name": "styleIdForFill", "type": 94, "array": False, "value": 332},
                333: {"name": "styleIdForStrokeFill", "type": 94, "array": False, "value": 333},
                334: {"name": "styleIdForText", "type": 94, "array": False, "value": 334},
                335: {"name": "styleIdForEffect", "type": 94, "array": False, "value": 335},
                336: {"name": "styleIdForGrid", "type": 94, "array": False, "value": 336},
                193: {"name": "backgroundPaints", "type": 72, "array": True, "value": 193},
                194: {
                    "name": "inheritFillStyleIDForBackground",
                    "type": 47,
                    "array": False,
                    "value": 194,
                },
                225: {"name": "isStateGroup", "type": -1, "array": False, "value": 225},
                238: {
                    "name": "stateGroupPropertyValueOrders",
                    "type": 200,
                    "array": True,
                    "value": 238,
                },
                122: {"name": "sharedSymbolReference", "type": 101, "array": False, "value": 122},
                123: {"name": "isSymbolPublishable", "type": -1, "array": False, "value": 123},
                124: {"name": "sharedSymbolMappings", "type": 86, "array": True, "value": 124},
                126: {"name": "sharedSymbolVersion", "type": -6, "array": False, "value": 126},
                152: {
                    "name": "sharedComponentMasterData",
                    "type": 102,
                    "array": False,
                    "value": 152,
                },
                144: {"name": "symbolDescription", "type": -6, "array": False, "value": 144},
                164: {"name": "unflatteningMappings", "type": 86, "array": True, "value": 164},
                228: {
                    "name": "forceUnflatteningMappings",
                    "type": 86,
                    "array": True,
                    "value": 228,
                },
                214: {"name": "publishFile", "type": -6, "array": False, "value": 214},
                215: {"name": "publishID", "type": 47, "array": False, "value": 215},
                216: {"name": "componentKey", "type": -6, "array": False, "value": 216},
                217: {"name": "isC2", "type": -1, "array": False, "value": 217},
                218: {"name": "publishedVersion", "type": -6, "array": False, "value": 218},
                252: {"name": "originComponentKey", "type": -6, "array": False, "value": 252},
                266: {"name": "componentPropDefs", "type": 185, "array": True, "value": 266},
                267: {"name": "componentPropRefs", "type": 182, "array": True, "value": 267},
                113: {"name": "symbolData", "type": 85, "array": False, "value": 113},
                114: {"name": "symbolDataTag", "type": -4, "array": False, "value": 114},
                125: {"name": "derivedSymbolData", "type": 152, "array": True, "value": 125},
                143: {"name": "overriddenSymbolID", "type": 47, "array": False, "value": 143},
                268: {
                    "name": "componentPropAssignments",
                    "type": 184,
                    "array": True,
                    "value": 268,
                },
                305: {"name": "propsAreBubbled", "type": -1, "array": False, "value": 305},
                248: {"name": "overrideStash", "type": 103, "array": True, "value": 248},
                250: {"name": "overrideStashV2", "type": 104, "array": True, "value": 250},
                111: {"name": "guidPath", "type": 84, "array": False, "value": 111},
                112: {"name": "guidPathTag", "type": -4, "array": False, "value": 112},
                321: {"name": "overrideLevel", "type": -3, "array": False, "value": 321},
                382: {"name": "moduleType", "type": 149, "array": False, "value": 382},
                21: {"name": "fontSize", "type": -5, "array": False, "value": 21},
                73: {"name": "fontSizeTag", "type": -4, "array": False, "value": 73},
                22: {"name": "paragraphIndent", "type": -5, "array": False, "value": 22},
                74: {"name": "paragraphIndentTag", "type": -4, "array": False, "value": 74},
                23: {"name": "paragraphSpacing", "type": -5, "array": False, "value": 23},
                75: {"name": "paragraphSpacingTag", "type": -4, "array": False, "value": 75},
                32: {"name": "textAlignHorizontal", "type": 20, "array": False, "value": 32},
                84: {"name": "textAlignHorizontalTag", "type": -4, "array": False, "value": 84},
                33: {"name": "textAlignVertical", "type": 21, "array": False, "value": 33},
                85: {"name": "textAlignVerticalTag", "type": -4, "array": False, "value": 85},
                34: {"name": "textCase", "type": 11, "array": False, "value": 34},
                86: {"name": "textCaseTag", "type": -4, "array": False, "value": 86},
                35: {"name": "textDecoration", "type": 12, "array": False, "value": 35},
                87: {"name": "textDecorationTag", "type": -4, "array": False, "value": 87},
                40: {"name": "lineHeight", "type": 54, "array": False, "value": 40},
                92: {"name": "lineHeightTag", "type": -4, "array": False, "value": 92},
                41: {"name": "fontName", "type": 55, "array": False, "value": 41},
                93: {"name": "fontNameTag", "type": -4, "array": False, "value": 93},
                42: {"name": "textData", "type": 75, "array": False, "value": 42},
                94: {"name": "textDataTag", "type": -4, "array": False, "value": 94},
                359: {"name": "derivedTextData", "type": 76, "array": False, "value": 359},
                127: {
                    "name": "fontVariantCommonLigatures",
                    "type": -1,
                    "array": False,
                    "value": 127,
                },
                128: {
                    "name": "fontVariantContextualLigatures",
                    "type": -1,
                    "array": False,
                    "value": 128,
                },
                129: {
                    "name": "fontVariantDiscretionaryLigatures",
                    "type": -1,
                    "array": False,
                    "value": 129,
                },
                130: {
                    "name": "fontVariantHistoricalLigatures",
                    "type": -1,
                    "array": False,
                    "value": 130,
                },
                131: {"name": "fontVariantOrdinal", "type": -1, "array": False, "value": 131},
                132: {"name": "fontVariantSlashedZero", "type": -1, "array": False, "value": 132},
                133: {
                    "name": "fontVariantNumericFigure",
                    "type": 56,
                    "array": False,
                    "value": 133,
                },
                134: {
                    "name": "fontVariantNumericSpacing",
                    "type": 57,
                    "array": False,
                    "value": 134,
                },
                135: {
                    "name": "fontVariantNumericFraction",
                    "type": 58,
                    "array": False,
                    "value": 135,
                },
                136: {"name": "fontVariantCaps", "type": 59, "array": False, "value": 136},
                137: {"name": "fontVariantPosition", "type": 60, "array": False, "value": 137},
                165: {"name": "letterSpacing", "type": 54, "array": False, "value": 165},
                202: {"name": "fontVersion", "type": -6, "array": False, "value": 202},
                322: {"name": "leadingTrim", "type": 13, "array": False, "value": 322},
                337: {"name": "hangingPunctuation", "type": -1, "array": False, "value": 337},
                339: {"name": "hangingList", "type": -1, "array": False, "value": 339},
                351: {"name": "maxLines", "type": -3, "array": False, "value": 351},
                352: {"name": "sectionStatus", "type": 150, "array": False, "value": 352},
                355: {"name": "sectionStatusInfo", "type": 151, "array": False, "value": 355},
                203: {"name": "textUserLayoutVersion", "type": -4, "array": False, "value": 203},
                205: {"name": "toggledOnOTFeatures", "type": 64, "array": True, "value": 205},
                206: {"name": "toggledOffOTFeatures", "type": 64, "array": True, "value": 206},
                223: {"name": "hyperlink", "type": 217, "array": False, "value": 223},
                340: {"name": "mention", "type": 219, "array": False, "value": 340},
                260: {"name": "fontVariations", "type": 74, "array": True, "value": 260},
                279: {"name": "textBidiVersion", "type": -4, "array": False, "value": 279},
                280: {"name": "textTruncation", "type": 30, "array": False, "value": 280},
                292: {"name": "hasHadRTLText", "type": -1, "array": False, "value": 292},
                6: {"name": "visible", "type": -1, "array": False, "value": 6},
                58: {"name": "visibleTag", "type": -4, "array": False, "value": 58},
                7: {"name": "locked", "type": -1, "array": False, "value": 7},
                59: {"name": "lockedTag", "type": -4, "array": False, "value": 59},
                8: {"name": "opacity", "type": -5, "array": False, "value": 8},
                60: {"name": "opacityTag", "type": -4, "array": False, "value": 60},
                9: {"name": "blendMode", "type": 7, "array": False, "value": 9},
                61: {"name": "blendModeTag", "type": -4, "array": False, "value": 61},
                11: {"name": "size", "type": 49, "array": False, "value": 11},
                63: {"name": "sizeTag", "type": -4, "array": False, "value": 63},
                12: {"name": "transform", "type": 52, "array": False, "value": 12},
                64: {"name": "transformTag", "type": -4, "array": False, "value": 64},
                13: {"name": "dashPattern", "type": -5, "array": True, "value": 13},
                65: {"name": "dashPatternTag", "type": -4, "array": False, "value": 65},
                16: {"name": "mask", "type": -1, "array": False, "value": 16},
                68: {"name": "maskTag", "type": -4, "array": False, "value": 68},
                18: {"name": "maskIsOutline", "type": -1, "array": False, "value": 18},
                70: {"name": "maskIsOutlineTag", "type": -4, "array": False, "value": 70},
                317: {"name": "maskType", "type": 148, "array": False, "value": 317},
                19: {"name": "backgroundOpacity", "type": -5, "array": False, "value": 19},
                71: {"name": "backgroundOpacityTag", "type": -4, "array": False, "value": 71},
                20: {"name": "cornerRadius", "type": -5, "array": False, "value": 20},
                72: {"name": "cornerRadiusTag", "type": -4, "array": False, "value": 72},
                26: {"name": "strokeWeight", "type": -5, "array": False, "value": 26},
                78: {"name": "strokeWeightTag", "type": -4, "array": False, "value": 78},
                29: {"name": "strokeAlign", "type": 16, "array": False, "value": 29},
                81: {"name": "strokeAlignTag", "type": -4, "array": False, "value": 81},
                30: {"name": "strokeCap", "type": 17, "array": False, "value": 30},
                82: {"name": "strokeCapTag", "type": -4, "array": False, "value": 82},
                31: {"name": "strokeJoin", "type": 18, "array": False, "value": 31},
                83: {"name": "strokeJoinTag", "type": -4, "array": False, "value": 83},
                38: {"name": "fillPaints", "type": 72, "array": True, "value": 38},
                90: {"name": "fillPaintsTag", "type": -4, "array": False, "value": 90},
                39: {"name": "strokePaints", "type": 72, "array": True, "value": 39},
                91: {"name": "strokePaintsTag", "type": -4, "array": False, "value": 91},
                43: {"name": "effects", "type": 105, "array": True, "value": 43},
                95: {"name": "effectsTag", "type": -4, "array": False, "value": 95},
                50: {"name": "backgroundColor", "type": 48, "array": False, "value": 50},
                102: {"name": "backgroundColorTag", "type": -4, "array": False, "value": 102},
                51: {"name": "fillGeometry", "type": 120, "array": True, "value": 51},
                103: {"name": "fillGeometryTag", "type": -4, "array": False, "value": 103},
                52: {"name": "strokeGeometry", "type": 120, "array": True, "value": 52},
                104: {"name": "strokeGeometryTag", "type": -4, "array": False, "value": 104},
                145: {
                    "name": "rectangleTopLeftCornerRadius",
                    "type": -5,
                    "array": False,
                    "value": 145,
                },
                146: {
                    "name": "rectangleTopRightCornerRadius",
                    "type": -5,
                    "array": False,
                    "value": 146,
                },
                147: {
                    "name": "rectangleBottomLeftCornerRadius",
                    "type": -5,
                    "array": False,
                    "value": 147,
                },
                148: {
                    "name": "rectangleBottomRightCornerRadius",
                    "type": -5,
                    "array": False,
                    "value": 148,
                },
                149: {
                    "name": "rectangleCornerRadiiIndependent",
                    "type": -1,
                    "array": False,
                    "value": 149,
                },
                150: {
                    "name": "rectangleCornerToolIndependent",
                    "type": -1,
                    "array": False,
                    "value": 150,
                },
                151: {"name": "proportionsConstrained", "type": -1, "array": False, "value": 151},
                258: {"name": "useAbsoluteBounds", "type": -1, "array": False, "value": 258},
                287: {"name": "borderTopHidden", "type": -1, "array": False, "value": 287},
                288: {"name": "borderBottomHidden", "type": -1, "array": False, "value": 288},
                289: {"name": "borderLeftHidden", "type": -1, "array": False, "value": 289},
                290: {"name": "borderRightHidden", "type": -1, "array": False, "value": 290},
                294: {"name": "bordersTakeSpace", "type": -1, "array": False, "value": 294},
                295: {"name": "borderTopWeight", "type": -5, "array": False, "value": 295},
                296: {"name": "borderBottomWeight", "type": -5, "array": False, "value": 296},
                297: {"name": "borderLeftWeight", "type": -5, "array": False, "value": 297},
                298: {"name": "borderRightWeight", "type": -5, "array": False, "value": 298},
                299: {
                    "name": "borderStrokeWeightsIndependent",
                    "type": -1,
                    "array": False,
                    "value": 299,
                },
                28: {"name": "horizontalConstraint", "type": 15, "array": False, "value": 28},
                80: {"name": "horizontalConstraintTag", "type": -4, "array": False, "value": 80},
                105: {"name": "stackMode", "type": 33, "array": False, "value": 105},
                106: {"name": "stackModeTag", "type": -4, "array": False, "value": 106},
                107: {"name": "stackSpacing", "type": -5, "array": False, "value": 107},
                108: {"name": "stackSpacingTag", "type": -4, "array": False, "value": 108},
                109: {"name": "stackPadding", "type": -5, "array": False, "value": 109},
                110: {"name": "stackPaddingTag", "type": -4, "array": False, "value": 110},
                120: {"name": "stackCounterAlign", "type": 35, "array": False, "value": 120},
                121: {"name": "stackJustify", "type": 36, "array": False, "value": 121},
                208: {"name": "stackAlign", "type": 34, "array": False, "value": 208},
                209: {"name": "stackHorizontalPadding", "type": -5, "array": False, "value": 209},
                210: {"name": "stackVerticalPadding", "type": -5, "array": False, "value": 210},
                211: {"name": "stackWidth", "type": 37, "array": False, "value": 211},
                212: {"name": "stackHeight", "type": 37, "array": False, "value": 212},
                229: {"name": "stackPrimarySizing", "type": 37, "array": False, "value": 229},
                230: {"name": "stackPrimaryAlignItems", "type": 36, "array": False, "value": 230},
                231: {"name": "stackCounterAlignItems", "type": 34, "array": False, "value": 231},
                232: {"name": "stackChildPrimaryGrow", "type": -5, "array": False, "value": 232},
                233: {"name": "stackPaddingRight", "type": -5, "array": False, "value": 233},
                234: {"name": "stackPaddingBottom", "type": -5, "array": False, "value": 234},
                236: {"name": "stackChildAlignSelf", "type": 35, "array": False, "value": 236},
                269: {"name": "stackPositioning", "type": 38, "array": False, "value": 269},
                271: {"name": "stackReverseZIndex", "type": -1, "array": False, "value": 271},
                323: {"name": "stackWrap", "type": 39, "array": False, "value": 323},
                324: {"name": "stackCounterSpacing", "type": -5, "array": False, "value": 324},
                325: {"name": "minSize", "type": 275, "array": False, "value": 325},
                326: {"name": "maxSize", "type": 275, "array": False, "value": 326},
                343: {
                    "name": "stackCounterAlignContent",
                    "type": 40,
                    "array": False,
                    "value": 343,
                },
                344: {"name": "isSnakeGameBoard", "type": -1, "array": False, "value": 344},
                139: {"name": "transitionNodeID", "type": 47, "array": False, "value": 139},
                140: {"name": "prototypeStartNodeID", "type": 47, "array": False, "value": 140},
                141: {
                    "name": "prototypeBackgroundColor",
                    "type": 48,
                    "array": False,
                    "value": 141,
                },
                153: {"name": "transitionInfo", "type": 106, "array": False, "value": 153},
                154: {"name": "transitionType", "type": 43, "array": False, "value": 154},
                155: {"name": "transitionDuration", "type": -5, "array": False, "value": 155},
                156: {"name": "easingType", "type": 44, "array": False, "value": 156},
                181: {
                    "name": "transitionPreserveScroll",
                    "type": -1,
                    "array": False,
                    "value": 181,
                },
                182: {"name": "connectionType", "type": 41, "array": False, "value": 182},
                183: {"name": "connectionURL", "type": -6, "array": False, "value": 183},
                184: {"name": "prototypeDevice", "type": 109, "array": False, "value": 184},
                187: {"name": "interactionType", "type": 42, "array": False, "value": 187},
                188: {"name": "transitionTimeout", "type": -5, "array": False, "value": 188},
                189: {"name": "interactionMaintained", "type": -1, "array": False, "value": 189},
                190: {"name": "interactionDuration", "type": -5, "array": False, "value": 190},
                192: {"name": "destinationIsOverlay", "type": -1, "array": False, "value": 192},
                207: {
                    "name": "transitionShouldSmartAnimate",
                    "type": -1,
                    "array": False,
                    "value": 207,
                },
                226: {"name": "prototypeInteractions", "type": 209, "array": True, "value": 226},
                249: {"name": "prototypeStartingPoint", "type": 214, "array": False, "value": 249},
                204: {"name": "pluginData", "type": 127, "array": True, "value": 204},
                219: {"name": "pluginRelaunchData", "type": 128, "array": True, "value": 219},
                242: {"name": "connectorStart", "type": 131, "array": False, "value": 242},
                243: {"name": "connectorEnd", "type": 131, "array": False, "value": 243},
                244: {"name": "connectorLineStyle", "type": 135, "array": False, "value": 244},
                245: {"name": "connectorStartCap", "type": 17, "array": False, "value": 245},
                246: {"name": "connectorEndCap", "type": 17, "array": False, "value": 246},
                253: {"name": "connectorControlPoints", "type": 132, "array": True, "value": 253},
                255: {"name": "connectorTextMidpoint", "type": 134, "array": False, "value": 255},
                373: {"name": "connectorType", "type": 136, "array": False, "value": 373},
                369: {"name": "annotations", "type": 139, "array": True, "value": 369},
                384: {"name": "measurements", "type": 141, "array": True, "value": 384},
                241: {"name": "shapeWithTextType", "type": 6, "array": False, "value": 241},
                247: {"name": "shapeUserHeight", "type": -5, "array": False, "value": 247},
                254: {
                    "name": "derivedImmutableFrameData",
                    "type": 88,
                    "array": False,
                    "value": 254,
                },
                338: {
                    "name": "derivedImmutableFrameDataVersion",
                    "type": 129,
                    "array": False,
                    "value": 338,
                },
                240: {"name": "nodeGenerationData", "type": 87, "array": False, "value": 240},
                259: {"name": "codeBlockLanguage", "type": 197, "array": False, "value": 259},
                278: {"name": "linkPreviewData", "type": 222, "array": False, "value": 278},
                282: {"name": "shapeTruncates", "type": -1, "array": False, "value": 282},
                283: {"name": "sectionContentsHidden", "type": -1, "array": False, "value": 283},
                300: {"name": "videoPlayback", "type": 153, "array": False, "value": 300},
                301: {"name": "stampData", "type": 221, "array": False, "value": 301},
                370: {"name": "sectionPresetInfo", "type": 295, "array": False, "value": 370},
                273: {"name": "widgetSyncedState", "type": 157, "array": False, "value": 273},
                274: {"name": "widgetSyncCursor", "type": -4, "array": False, "value": 274},
                275: {
                    "name": "widgetDerivedSubtreeCursor",
                    "type": 156,
                    "array": False,
                    "value": 275,
                },
                276: {"name": "widgetCachedAncestor", "type": 145, "array": False, "value": 276},
                285: {"name": "widgetInputBehavior", "type": 192, "array": False, "value": 285},
                286: {"name": "widgetTooltip", "type": -6, "array": False, "value": 286},
                291: {"name": "widgetHoverStyle", "type": 155, "array": False, "value": 291},
                293: {"name": "isWidgetStickable", "type": -1, "array": False, "value": 293},
                360: {
                    "name": "shouldHideCursorsOnWidgetHover",
                    "type": -1,
                    "array": False,
                    "value": 360,
                },
                262: {"name": "widgetMetadata", "type": 193, "array": False, "value": 262},
                263: {"name": "widgetEvents", "type": 191, "array": True, "value": 263},
                265: {"name": "widgetPropertyMenuItems", "type": 196, "array": True, "value": 265},
                308: {"name": "tableRowPositions", "type": 166, "array": False, "value": 308},
                309: {"name": "tableColumnPositions", "type": 166, "array": False, "value": 309},
                310: {"name": "tableRowHeights", "type": 168, "array": False, "value": 310},
                311: {"name": "tableColumnWidths", "type": 168, "array": False, "value": 311},
                371: {
                    "name": "interactiveSlideConfigData",
                    "type": 157,
                    "array": False,
                    "value": 371,
                },
                372: {
                    "name": "interactiveSlideParticipantData",
                    "type": 157,
                    "array": False,
                    "value": 372,
                },
                379: {"name": "themeID", "type": 99, "array": False, "value": 379},
                381: {"name": "slideThemeData", "type": 100, "array": False, "value": 381},
                363: {"name": "diagramParentId", "type": 47, "array": False, "value": 363},
                362: {"name": "layoutRoot", "type": 47, "array": False, "value": 362},
                364: {"name": "layoutPosition", "type": -6, "array": False, "value": 364},
                366: {"name": "diagramLayoutRuleType", "type": 179, "array": False, "value": 366},
                367: {"name": "diagramParentIndex", "type": 180, "array": False, "value": 367},
                368: {"name": "diagramLayoutPaused", "type": 181, "array": False, "value": 368},
                380: {"name": "isPageDivider", "type": -1, "array": False, "value": 380},
                251: {"name": "internalEnumForTest", "type": 198, "array": False, "value": 251},
                257: {"name": "internalDataForTest", "type": 199, "array": False, "value": 257},
                10: {"name": "count", "type": -4, "array": False, "value": 10},
                62: {"name": "countTag", "type": -4, "array": False, "value": 62},
                14: {"name": "autoRename", "type": -1, "array": False, "value": 14},
                66: {"name": "autoRenameTag", "type": -4, "array": False, "value": 66},
                15: {"name": "backgroundEnabled", "type": -1, "array": False, "value": 15},
                67: {"name": "backgroundEnabledTag", "type": -4, "array": False, "value": 67},
                17: {"name": "exportContentsOnly", "type": -1, "array": False, "value": 17},
                69: {"name": "exportContentsOnlyTag", "type": -4, "array": False, "value": 69},
                24: {"name": "starInnerScale", "type": -5, "array": False, "value": 24},
                76: {"name": "starInnerScaleTag", "type": -4, "array": False, "value": 76},
                25: {"name": "miterLimit", "type": -5, "array": False, "value": 25},
                77: {"name": "miterLimitTag", "type": -4, "array": False, "value": 77},
                27: {"name": "textTracking", "type": -5, "array": False, "value": 27},
                79: {"name": "textTrackingTag", "type": -4, "array": False, "value": 79},
                36: {"name": "booleanOperation", "type": 19, "array": False, "value": 36},
                88: {"name": "booleanOperationTag", "type": -4, "array": False, "value": 88},
                37: {"name": "verticalConstraint", "type": 15, "array": False, "value": 37},
                89: {"name": "verticalConstraintTag", "type": -4, "array": False, "value": 89},
                44: {"name": "handleMirroring", "type": 23, "array": False, "value": 44},
                96: {"name": "handleMirroringTag", "type": -4, "array": False, "value": 96},
                45: {"name": "exportSettings", "type": 116, "array": True, "value": 45},
                97: {"name": "exportSettingsTag", "type": -4, "array": False, "value": 97},
                46: {"name": "textAutoResize", "type": 29, "array": False, "value": 46},
                98: {"name": "textAutoResizeTag", "type": -4, "array": False, "value": 98},
                47: {"name": "layoutGrids", "type": 118, "array": True, "value": 47},
                99: {"name": "layoutGridsTag", "type": -4, "array": False, "value": 99},
                48: {"name": "vectorData", "type": 83, "array": False, "value": 48},
                100: {"name": "vectorDataTag", "type": -4, "array": False, "value": 100},
                115: {"name": "frameMaskDisabled", "type": -1, "array": False, "value": 115},
                116: {"name": "frameMaskDisabledTag", "type": -4, "array": False, "value": 116},
                117: {"name": "resizeToFit", "type": -1, "array": False, "value": 117},
                118: {"name": "resizeToFitTag", "type": -4, "array": False, "value": 118},
                119: {
                    "name": "exportBackgroundDisabled",
                    "type": -1,
                    "array": False,
                    "value": 119,
                },
                138: {"name": "guides", "type": 119, "array": True, "value": 138},
                142: {"name": "internalOnly", "type": -1, "array": False, "value": 142},
                159: {"name": "scrollDirection", "type": 45, "array": False, "value": 159},
                160: {"name": "cornerSmoothing", "type": -5, "array": False, "value": 160},
                166: {"name": "scrollOffset", "type": 49, "array": False, "value": 166},
                175: {"name": "exportTextAsSVGText", "type": -1, "array": False, "value": 175},
                178: {"name": "scrollContractedState", "type": 46, "array": False, "value": 178},
                179: {"name": "contractedSize", "type": 49, "array": False, "value": 179},
                180: {"name": "fixedChildrenDivider", "type": -6, "array": False, "value": 180},
                186: {"name": "scrollBehavior", "type": 124, "array": False, "value": 186},
                195: {"name": "arcData", "type": 125, "array": False, "value": 195},
                196: {
                    "name": "derivedSymbolDataLayoutVersion",
                    "type": -3,
                    "array": False,
                    "value": 196,
                },
                197: {"name": "navigationType", "type": 114, "array": False, "value": 197},
                198: {"name": "overlayPositionType", "type": 110, "array": False, "value": 198},
                199: {"name": "overlayRelativePosition", "type": 49, "array": False, "value": 199},
                200: {
                    "name": "overlayBackgroundInteraction",
                    "type": 111,
                    "array": False,
                    "value": 200,
                },
                201: {
                    "name": "overlayBackgroundAppearance",
                    "type": 113,
                    "array": False,
                    "value": 201,
                },
                213: {"name": "overrideKey", "type": 47, "array": False, "value": 213},
                220: {
                    "name": "containerSupportsFillStrokeAndCorners",
                    "type": -1,
                    "array": False,
                    "value": 220,
                },
                221: {"name": "stackCounterSizing", "type": 37, "array": False, "value": 221},
                222: {
                    "name": "containersSupportFillStrokeAndCorners",
                    "type": -1,
                    "array": False,
                    "value": 222,
                },
                224: {"name": "keyTrigger", "type": 216, "array": False, "value": 224},
                227: {"name": "voiceEventPhrase", "type": -6, "array": False, "value": 227},
                235: {
                    "name": "ancestorPathBeforeDeletion",
                    "type": 47,
                    "array": True,
                    "value": 235,
                },
                237: {"name": "symbolLinks", "type": 126, "array": True, "value": 237},
                239: {"name": "textListData", "type": 201, "array": False, "value": 239},
                261: {
                    "name": "detachOpticalSizeFromFontSize",
                    "type": -1,
                    "array": False,
                    "value": 261,
                },
                264: {"name": "listSpacing", "type": -5, "array": False, "value": 264},
                270: {"name": "embedData", "type": 220, "array": False, "value": 270},
                272: {"name": "richMediaData", "type": 260, "array": False, "value": 272},
                277: {"name": "renderedSyncedState", "type": 157, "array": False, "value": 277},
                284: {"name": "simplifyInstancePanels", "type": -1, "array": False, "value": 284},
                302: {"name": "accessibleHTMLTag", "type": 276, "array": False, "value": 302},
                303: {"name": "ariaRole", "type": 277, "array": False, "value": 303},
                304: {"name": "accessibleLabel", "type": -6, "array": False, "value": 304},
                306: {"name": "variableData", "type": 269, "array": False, "value": 306},
                307: {"name": "variableConsumptionMap", "type": 159, "array": False, "value": 307},
                316: {"name": "variableModeBySetMap", "type": 162, "array": False, "value": 316},
                312: {"name": "variableSetModes", "type": 270, "array": True, "value": 312},
                313: {"name": "variableSetID", "type": 98, "array": False, "value": 313},
                314: {"name": "variableResolvedType", "type": 262, "array": False, "value": 314},
                315: {"name": "variableDataValues", "type": 271, "array": False, "value": 315},
                350: {"name": "variableTokenName", "type": -6, "array": False, "value": 350},
                353: {"name": "variableScopes", "type": 273, "array": True, "value": 353},
                358: {"name": "codeSyntax", "type": 164, "array": False, "value": 358},
                377: {"name": "backingVariableSetId", "type": 98, "array": False, "value": 377},
                378: {"name": "backingVariableId", "type": 296, "array": False, "value": 378},
                385: {"name": "isCollectionExtendable", "type": -1, "array": False, "value": 385},
                386: {"name": "rootVariableKey", "type": -6, "array": False, "value": 386},
                361: {"name": "handoffStatusMap", "type": 290, "array": False, "value": 361},
                327: {"name": "agendaPositionMap", "type": 170, "array": False, "value": 327},
                328: {"name": "agendaMetadataMap", "type": 173, "array": False, "value": 328},
                329: {"name": "migrationStatus", "type": 278, "array": False, "value": 329},
                330: {"name": "isSoftDeleted", "type": -1, "array": False, "value": 330},
                331: {"name": "editInfo", "type": 146, "array": False, "value": 331},
                341: {"name": "colorProfile", "type": 281, "array": False, "value": 341},
                342: {"name": "detachedSymbolId", "type": 95, "array": False, "value": 342},
                346: {"name": "childReadingDirection", "type": 283, "array": False, "value": 346},
                347: {"name": "readingIndex", "type": -6, "array": False, "value": 347},
                349: {"name": "documentColorProfile", "type": 282, "array": False, "value": 349},
                354: {"name": "developerRelatedLinks", "type": 144, "array": True, "value": 354},
                356: {"name": "slideActiveThemeLibKey", "type": -6, "array": False, "value": 356},
                357: {"name": "ariaAttributes", "type": 287, "array": False, "value": 357},
                365: {"name": "editScopeInfo", "type": 291, "array": False, "value": 365},
                374: {"name": "semanticWeight", "type": 62, "array": False, "value": 374},
                375: {"name": "semanticItalic", "type": 63, "array": False, "value": 375},
                387: {"name": "isResponsiveSet", "type": -1, "array": False, "value": 387},
            }
        ),
    },
    {
        "name": "VideoPlayback",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "autoplay", "type": -1, "array": False, "value": 1},
                2: {"name": "mediaLoop", "type": -1, "array": False, "value": 2},
                3: {"name": "muted", "type": -1, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "MediaAction",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "PLAY", "type": 0, "array": False, "value": 0},
                1: {"name": "PAUSE", "type": 0, "array": False, "value": 1},
                2: {"name": "TOGGLE_PLAY_PAUSE", "type": 0, "array": False, "value": 2},
                3: {"name": "MUTE", "type": 0, "array": False, "value": 3},
                4: {"name": "UNMUTE", "type": 0, "array": False, "value": 4},
                5: {"name": "TOGGLE_MUTE_UNMUTE", "type": 0, "array": False, "value": 5},
                6: {"name": "SKIP_FORWARD", "type": 0, "array": False, "value": 6},
                7: {"name": "SKIP_BACKWARD", "type": 0, "array": False, "value": 7},
                8: {"name": "SKIP_TO", "type": 0, "array": False, "value": 8},
            }
        ),
    },
    {
        "name": "WidgetHoverStyle",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "fillPaints", "type": 72, "array": True, "value": 1},
                2: {"name": "strokePaints", "type": 72, "array": True, "value": 2},
                3: {"name": "opacity", "type": -5, "array": False, "value": 3},
                4: {"name": "areFillPaintsSet", "type": -1, "array": False, "value": 4},
                5: {"name": "areStrokePaintsSet", "type": -1, "array": False, "value": 5},
                6: {"name": "isOpacitySet", "type": -1, "array": False, "value": 6},
            }
        ),
    },
    {
        "name": "WidgetDerivedSubtreeCursor",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "sessionID", "type": -4, "array": False, "value": 1},
                2: {"name": "counter", "type": -4, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "MultiplayerMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 158, "array": True, "value": 1}}),
    },
    {
        "name": "MultiplayerMapEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "key", "type": -6, "array": False, "value": 1},
                2: {"name": "value", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "VariableDataMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 160, "array": True, "value": 1}}),
    },
    {
        "name": "VariableDataMapEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "nodeField", "type": -4, "array": False, "value": 1},
                2: {"name": "variableData", "type": 269, "array": False, "value": 2},
                3: {"name": "variableField", "type": 161, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "VariableField",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "MISSING", "type": 0, "array": False, "value": 0},
                1: {"name": "CORNER_RADIUS", "type": 0, "array": False, "value": 1},
                2: {"name": "PARAGRAPH_SPACING", "type": 0, "array": False, "value": 2},
                3: {"name": "PARAGRAPH_INDENT", "type": 0, "array": False, "value": 3},
                4: {"name": "STROKE_WEIGHT", "type": 0, "array": False, "value": 4},
                5: {"name": "STACK_SPACING", "type": 0, "array": False, "value": 5},
                6: {"name": "STACK_PADDING_LEFT", "type": 0, "array": False, "value": 6},
                7: {"name": "STACK_PADDING_TOP", "type": 0, "array": False, "value": 7},
                8: {"name": "STACK_PADDING_RIGHT", "type": 0, "array": False, "value": 8},
                9: {"name": "STACK_PADDING_BOTTOM", "type": 0, "array": False, "value": 9},
                10: {"name": "VISIBLE", "type": 0, "array": False, "value": 10},
                11: {"name": "TEXT_DATA", "type": 0, "array": False, "value": 11},
                12: {"name": "WIDTH", "type": 0, "array": False, "value": 12},
                13: {"name": "HEIGHT", "type": 0, "array": False, "value": 13},
                14: {
                    "name": "RECTANGLE_TOP_LEFT_CORNER_RADIUS",
                    "type": 0,
                    "array": False,
                    "value": 14,
                },
                15: {
                    "name": "RECTANGLE_TOP_RIGHT_CORNER_RADIUS",
                    "type": 0,
                    "array": False,
                    "value": 15,
                },
                16: {
                    "name": "RECTANGLE_BOTTOM_LEFT_CORNER_RADIUS",
                    "type": 0,
                    "array": False,
                    "value": 16,
                },
                17: {
                    "name": "RECTANGLE_BOTTOM_RIGHT_CORNER_RADIUS",
                    "type": 0,
                    "array": False,
                    "value": 17,
                },
                18: {"name": "BORDER_TOP_WEIGHT", "type": 0, "array": False, "value": 18},
                19: {"name": "BORDER_BOTTOM_WEIGHT", "type": 0, "array": False, "value": 19},
                20: {"name": "BORDER_LEFT_WEIGHT", "type": 0, "array": False, "value": 20},
                21: {"name": "BORDER_RIGHT_WEIGHT", "type": 0, "array": False, "value": 21},
                22: {"name": "VARIANT_PROPERTIES", "type": 0, "array": False, "value": 22},
                23: {"name": "STACK_COUNTER_SPACING", "type": 0, "array": False, "value": 23},
                24: {"name": "MIN_WIDTH", "type": 0, "array": False, "value": 24},
                25: {"name": "MAX_WIDTH", "type": 0, "array": False, "value": 25},
                26: {"name": "MIN_HEIGHT", "type": 0, "array": False, "value": 26},
                27: {"name": "MAX_HEIGHT", "type": 0, "array": False, "value": 27},
                28: {"name": "FONT_FAMILY", "type": 0, "array": False, "value": 28},
                29: {"name": "FONT_STYLE", "type": 0, "array": False, "value": 29},
                30: {"name": "FONT_VARIATIONS", "type": 0, "array": False, "value": 30},
            }
        ),
    },
    {
        "name": "VariableModeBySetMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 163, "array": True, "value": 1}}),
    },
    {
        "name": "VariableModeBySetMapEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "variableSetID", "type": 98, "array": False, "value": 1},
                2: {"name": "variableModeID", "type": 47, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "CodeSyntaxMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 165, "array": True, "value": 1}}),
    },
    {
        "name": "CodeSyntaxMapEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "platform", "type": 274, "array": False, "value": 1},
                2: {"name": "value", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "TableRowColumnPositionMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 167, "array": True, "value": 1}}),
    },
    {
        "name": "TableRowColumnPositionMapEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "id", "type": 47, "array": False, "value": 1},
                2: {"name": "position", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "TableRowColumnSizeMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 169, "array": True, "value": 1}}),
    },
    {
        "name": "TableRowColumnSizeMapEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "id", "type": 47, "array": False, "value": 1},
                2: {"name": "size", "type": -5, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "AgendaPositionMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 171, "array": True, "value": 1}}),
    },
    {
        "name": "AgendaPositionMapEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "id", "type": 47, "array": False, "value": 1},
                2: {"name": "position", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "AgendaItemType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NODE", "type": 0, "array": False, "value": 0},
                1: {"name": "BLOCK", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "AgendaMetadataMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 174, "array": True, "value": 1}}),
    },
    {
        "name": "AgendaMetadataMapEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "id", "type": 47, "array": False, "value": 1},
                2: {"name": "data", "type": 175, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "AgendaMetadata",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "name", "type": -6, "array": False, "value": 1},
                2: {"name": "type", "type": 172, "array": False, "value": 2},
                3: {"name": "targetNodeID", "type": 47, "array": False, "value": 3},
                4: {"name": "timerInfo", "type": 176, "array": False, "value": 4},
                5: {"name": "voteInfo", "type": 177, "array": False, "value": 5},
                6: {"name": "musicInfo", "type": 178, "array": False, "value": 6},
            }
        ),
    },
    {
        "name": "AgendaTimerInfo",
        "kind": 2,
        "fields": OrderedDict(
            {1: {"name": "timerLength", "type": -4, "array": False, "value": 1}}
        ),
    },
    {
        "name": "AgendaVoteInfo",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "voteCount", "type": -4, "array": False, "value": 1}}),
    },
    {
        "name": "AgendaMusicInfo",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "songID", "type": -6, "array": False, "value": 1},
                2: {"name": "startTimeMs", "type": -4, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "DiagramLayoutRuleType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "TREE", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "DiagramParentIndex",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                2: {"name": "position", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "DiagramLayoutPaused",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NO", "type": 0, "array": False, "value": 0},
                1: {"name": "YES", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "ComponentPropRef",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "nodeField", "type": -4, "array": False, "value": 1},
                2: {"name": "defID", "type": 47, "array": False, "value": 2},
                3: {"name": "zombieFallbackName", "type": -6, "array": False, "value": 3},
                4: {"name": "componentPropNodeField", "type": 183, "array": False, "value": 4},
                5: {"name": "isDeleted", "type": -1, "array": False, "value": 5},
            }
        ),
    },
    {
        "name": "ComponentPropNodeField",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "VISIBLE", "type": 0, "array": False, "value": 0},
                1: {"name": "TEXT_DATA", "type": 0, "array": False, "value": 1},
                2: {"name": "OVERRIDDEN_SYMBOL_ID", "type": 0, "array": False, "value": 2},
                3: {"name": "INHERIT_FILL_STYLE_ID", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "ComponentPropAssignment",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "defID", "type": 47, "array": False, "value": 1},
                2: {"name": "value", "type": 186, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ComponentPropDef",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "id", "type": 47, "array": False, "value": 1},
                2: {"name": "name", "type": -6, "array": False, "value": 2},
                3: {"name": "initialValue", "type": 186, "array": False, "value": 3},
                4: {"name": "sortPosition", "type": -6, "array": False, "value": 4},
                5: {"name": "parentPropDefId", "type": 47, "array": False, "value": 5},
                6: {"name": "type", "type": 187, "array": False, "value": 6},
                7: {"name": "isDeleted", "type": -1, "array": False, "value": 7},
                8: {"name": "preferredValues", "type": 188, "array": False, "value": 8},
            }
        ),
    },
    {
        "name": "ComponentPropValue",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "boolValue", "type": -1, "array": False, "value": 1},
                2: {"name": "textValue", "type": 75, "array": False, "value": 2},
                3: {"name": "guidValue", "type": 47, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "ComponentPropType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "BOOL", "type": 0, "array": False, "value": 0},
                1: {"name": "TEXT", "type": 0, "array": False, "value": 1},
                2: {"name": "COLOR", "type": 0, "array": False, "value": 2},
                3: {"name": "INSTANCE_SWAP", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "ComponentPropPreferredValues",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "stringValues", "type": -6, "array": True, "value": 1},
                2: {"name": "instanceSwapValues", "type": 189, "array": True, "value": 2},
            }
        ),
    },
    {
        "name": "InstanceSwapPreferredValue",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "type", "type": 190, "array": False, "value": 1},
                2: {"name": "key", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "InstanceSwapPreferredValueType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "COMPONENT", "type": 0, "array": False, "value": 0},
                1: {"name": "STATE_GROUP", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "WidgetEvent",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "MOUSE_DOWN", "type": 0, "array": False, "value": 0},
                1: {"name": "CLICK", "type": 0, "array": False, "value": 1},
                2: {"name": "TEXT_EDIT_END", "type": 0, "array": False, "value": 2},
                3: {"name": "ATTACHED_STICKABLES_CHANGED", "type": 0, "array": False, "value": 3},
                4: {"name": "STUCK_STATUS_CHANGED", "type": 0, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "WidgetInputBehavior",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "WRAP", "type": 0, "array": False, "value": 0},
                1: {"name": "TRUNCATE", "type": 0, "array": False, "value": 1},
                2: {"name": "MULTILINE", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "WidgetMetadata",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "pluginID", "type": -6, "array": False, "value": 1},
                2: {"name": "pluginVersionID", "type": -6, "array": False, "value": 2},
                3: {"name": "widgetName", "type": -6, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "WidgetPropertyMenuItemType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "ACTION", "type": 0, "array": False, "value": 0},
                1: {"name": "SEPARATOR", "type": 0, "array": False, "value": 1},
                2: {"name": "COLOR", "type": 0, "array": False, "value": 2},
                3: {"name": "DROPDOWN", "type": 0, "array": False, "value": 3},
                4: {"name": "COLOR_SELECTOR", "type": 0, "array": False, "value": 4},
                5: {"name": "TOGGLE", "type": 0, "array": False, "value": 5},
                6: {"name": "LINK", "type": 0, "array": False, "value": 6},
            }
        ),
    },
    {
        "name": "WidgetPropertyMenuSelectorOption",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "option", "type": -6, "array": False, "value": 1},
                2: {"name": "tooltip", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "WidgetPropertyMenuItem",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "propertyName", "type": -6, "array": False, "value": 1},
                2: {"name": "tooltip", "type": -6, "array": False, "value": 2},
                3: {"name": "itemType", "type": 194, "array": False, "value": 3},
                4: {"name": "icon", "type": -6, "array": False, "value": 4},
                5: {"name": "options", "type": 195, "array": True, "value": 5},
                6: {"name": "selectedOption", "type": -6, "array": False, "value": 6},
                7: {"name": "isToggled", "type": -1, "array": False, "value": 7},
                8: {"name": "href", "type": -6, "array": False, "value": 8},
                9: {"name": "allowCustomColor", "type": -1, "array": False, "value": 9},
            }
        ),
    },
    {
        "name": "CodeBlockLanguage",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "TYPESCRIPT", "type": 0, "array": False, "value": 0},
                1: {"name": "CPP", "type": 0, "array": False, "value": 1},
                2: {"name": "RUBY", "type": 0, "array": False, "value": 2},
                3: {"name": "CSS", "type": 0, "array": False, "value": 3},
                4: {"name": "JAVASCRIPT", "type": 0, "array": False, "value": 4},
                5: {"name": "HTML", "type": 0, "array": False, "value": 5},
                6: {"name": "JSON", "type": 0, "array": False, "value": 6},
                7: {"name": "GRAPHQL", "type": 0, "array": False, "value": 7},
                8: {"name": "PYTHON", "type": 0, "array": False, "value": 8},
                9: {"name": "GO", "type": 0, "array": False, "value": 9},
                10: {"name": "SQL", "type": 0, "array": False, "value": 10},
                11: {"name": "SWIFT", "type": 0, "array": False, "value": 11},
                12: {"name": "KOTLIN", "type": 0, "array": False, "value": 12},
                13: {"name": "RUST", "type": 0, "array": False, "value": 13},
                14: {"name": "BASH", "type": 0, "array": False, "value": 14},
                15: {"name": "PLAINTEXT", "type": 0, "array": False, "value": 15},
            }
        ),
    },
    {
        "name": "InternalEnumForTest",
        "kind": 0,
        "fields": OrderedDict({1: {"name": "OLD", "type": 0, "array": False, "value": 1}}),
    },
    {
        "name": "InternalDataForTest",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "testFieldA", "type": -3, "array": False, "value": 1}}),
    },
    {
        "name": "StateGroupPropertyValueOrder",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "property", "type": -6, "array": False, "value": 1},
                2: {"name": "values", "type": -6, "array": True, "value": 2},
            }
        ),
    },
    {
        "name": "TextListData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "listID", "type": -3, "array": False, "value": 1},
                2: {"name": "bulletType", "type": 202, "array": False, "value": 2},
                3: {"name": "indentationLevel", "type": -3, "array": False, "value": 3},
                4: {"name": "lineNumber", "type": -3, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "BulletType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "ORDERED", "type": 0, "array": False, "value": 0},
                1: {"name": "UNORDERED", "type": 0, "array": False, "value": 1},
                2: {"name": "INDENT", "type": 0, "array": False, "value": 2},
                3: {"name": "NO_LIST", "type": 0, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "TextLineData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "lineType", "type": 205, "array": False, "value": 1},
                2: {"name": "indentationLevel", "type": -3, "array": False, "value": 2},
                9: {"name": "sourceDirectionality", "type": 206, "array": False, "value": 9},
                3: {"name": "directionality", "type": 207, "array": False, "value": 3},
                4: {"name": "directionalityIntent", "type": 208, "array": False, "value": 4},
                5: {"name": "downgradeStyleId", "type": -3, "array": False, "value": 5},
                6: {"name": "consistencyStyleId", "type": -3, "array": False, "value": 6},
                7: {"name": "listStartOffset", "type": -3, "array": False, "value": 7},
                8: {"name": "isFirstLineOfList", "type": -1, "array": False, "value": 8},
            }
        ),
    },
    {
        "name": "DerivedTextLineData",
        "kind": 2,
        "fields": OrderedDict(
            {1: {"name": "directionality", "type": 207, "array": False, "value": 1}}
        ),
    },
    {
        "name": "LineType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "PLAIN", "type": 0, "array": False, "value": 0},
                1: {"name": "ORDERED_LIST", "type": 0, "array": False, "value": 1},
                2: {"name": "UNORDERED_LIST", "type": 0, "array": False, "value": 2},
                3: {"name": "BLOCKQUOTE", "type": 0, "array": False, "value": 3},
                4: {"name": "HEADER", "type": 0, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "SourceDirectionality",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "AUTO", "type": 0, "array": False, "value": 0},
                1: {"name": "LTR", "type": 0, "array": False, "value": 1},
                2: {"name": "RTL", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "Directionality",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "LTR", "type": 0, "array": False, "value": 0},
                1: {"name": "RTL", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "DirectionalityIntent",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "IMPLICIT", "type": 0, "array": False, "value": 0},
                1: {"name": "EXPLICIT", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "PrototypeInteraction",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "id", "type": 47, "array": False, "value": 1},
                2: {"name": "event", "type": 210, "array": False, "value": 2},
                3: {"name": "actions", "type": 213, "array": True, "value": 3},
                4: {"name": "isDeleted", "type": -1, "array": False, "value": 4},
                5: {"name": "stateManagementVersion", "type": -3, "array": False, "value": 5},
            }
        ),
    },
    {
        "name": "PrototypeEvent",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "interactionType", "type": 42, "array": False, "value": 1},
                2: {"name": "interactionMaintained", "type": -1, "array": False, "value": 2},
                3: {"name": "interactionDuration", "type": -5, "array": False, "value": 3},
                4: {"name": "keyTrigger", "type": 216, "array": False, "value": 4},
                5: {"name": "voiceEventPhrase", "type": -6, "array": False, "value": 5},
                6: {"name": "transitionTimeout", "type": -5, "array": False, "value": 6},
                7: {"name": "mediaHitTime", "type": -5, "array": False, "value": 7},
            }
        ),
    },
    {
        "name": "PrototypeVariableTarget",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "id", "type": 96, "array": False, "value": 1}}),
    },
    {
        "name": "ConditionalActions",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "actions", "type": 213, "array": True, "value": 1},
                2: {"name": "condition", "type": 269, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "PrototypeAction",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "transitionNodeID", "type": 47, "array": False, "value": 1},
                2: {"name": "transitionType", "type": 43, "array": False, "value": 2},
                3: {"name": "transitionDuration", "type": -5, "array": False, "value": 3},
                4: {"name": "easingType", "type": 44, "array": False, "value": 4},
                5: {"name": "transitionTimeout", "type": -5, "array": False, "value": 5},
                6: {
                    "name": "transitionShouldSmartAnimate",
                    "type": -1,
                    "array": False,
                    "value": 6,
                },
                7: {"name": "connectionType", "type": 41, "array": False, "value": 7},
                8: {"name": "connectionURL", "type": -6, "array": False, "value": 8},
                9: {"name": "overlayRelativePosition", "type": 49, "array": False, "value": 9},
                10: {"name": "navigationType", "type": 114, "array": False, "value": 10},
                11: {"name": "transitionPreserveScroll", "type": -1, "array": False, "value": 11},
                12: {"name": "easingFunction", "type": -5, "array": True, "value": 12},
                13: {"name": "extraScrollOffset", "type": 49, "array": False, "value": 13},
                14: {"name": "targetVariableID", "type": 47, "array": False, "value": 14},
                15: {"name": "targetVariableValue", "type": 263, "array": False, "value": 15},
                16: {"name": "mediaAction", "type": 154, "array": False, "value": 16},
                17: {
                    "name": "transitionResetVideoPosition",
                    "type": -1,
                    "array": False,
                    "value": 17,
                },
                18: {"name": "openUrlInNewTab", "type": -1, "array": False, "value": 18},
                19: {"name": "targetVariable", "type": 211, "array": False, "value": 19},
                20: {"name": "targetVariableData", "type": 269, "array": False, "value": 20},
                21: {"name": "mediaSkipToTime", "type": -5, "array": False, "value": 21},
                22: {"name": "mediaSkipByAmount", "type": -5, "array": False, "value": 22},
                23: {"name": "conditions", "type": 269, "array": True, "value": 23},
                24: {"name": "conditionalActions", "type": 212, "array": True, "value": 24},
                25: {
                    "name": "transitionResetScrollPosition",
                    "type": -1,
                    "array": False,
                    "value": 25,
                },
                26: {
                    "name": "transitionResetInteractiveComponents",
                    "type": -1,
                    "array": False,
                    "value": 26,
                },
            }
        ),
    },
    {
        "name": "PrototypeStartingPoint",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "name", "type": -6, "array": False, "value": 1},
                2: {"name": "description", "type": -6, "array": False, "value": 2},
                3: {"name": "position", "type": -6, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "TriggerDevice",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "KEYBOARD", "type": 0, "array": False, "value": 0},
                1: {"name": "UNKNOWN_CONTROLLER", "type": 0, "array": False, "value": 1},
                2: {"name": "XBOX_ONE", "type": 0, "array": False, "value": 2},
                3: {"name": "PS4", "type": 0, "array": False, "value": 3},
                4: {"name": "SWITCH_PRO", "type": 0, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "KeyTrigger",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "keyCodes", "type": -3, "array": True, "value": 1},
                2: {"name": "triggerDevice", "type": 215, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "Hyperlink",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "url", "type": -6, "array": False, "value": 1},
                2: {"name": "guid", "type": 47, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "MentionSource",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "DEFAULT", "type": 0, "array": False, "value": 0},
                1: {"name": "COPY_DUPLICATE", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "Mention",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "id", "type": 47, "array": False, "value": 1},
                2: {"name": "mentionedUserId", "type": -6, "array": False, "value": 2},
                3: {"name": "mentionedByUserId", "type": -6, "array": False, "value": 3},
                4: {"name": "fileKey", "type": -6, "array": False, "value": 4},
                5: {"name": "source", "type": 218, "array": False, "value": 5},
                6: {"name": "mentionedUserIdInt", "type": -8, "array": False, "value": 6},
                7: {"name": "mentionedByUserIdInt", "type": -8, "array": False, "value": 7},
            }
        ),
    },
    {
        "name": "EmbedData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "url", "type": -6, "array": False, "value": 1},
                2: {"name": "srcUrl", "type": -6, "array": False, "value": 2},
                3: {"name": "title", "type": -6, "array": False, "value": 3},
                4: {"name": "thumbnailUrl", "type": -6, "array": False, "value": 4},
                5: {"name": "width", "type": -5, "array": False, "value": 5},
                6: {"name": "height", "type": -5, "array": False, "value": 6},
                7: {"name": "embedType", "type": -6, "array": False, "value": 7},
                8: {"name": "thumbnailImageHash", "type": -6, "array": False, "value": 8},
                9: {"name": "faviconImageHash", "type": -6, "array": False, "value": 9},
                10: {"name": "provider", "type": -6, "array": False, "value": 10},
                11: {"name": "originalText", "type": -6, "array": False, "value": 11},
                12: {"name": "description", "type": -6, "array": False, "value": 12},
                13: {"name": "embedVersionId", "type": -6, "array": False, "value": 13},
            }
        ),
    },
    {
        "name": "StampData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "userId", "type": -6, "array": False, "value": 1},
                2: {"name": "votingSessionId", "type": -6, "array": False, "value": 2},
                3: {"name": "stampedByUserId", "type": -6, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "LinkPreviewData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "url", "type": -6, "array": False, "value": 1},
                2: {"name": "title", "type": -6, "array": False, "value": 2},
                3: {"name": "provider", "type": -6, "array": False, "value": 3},
                4: {"name": "description", "type": -6, "array": False, "value": 4},
                5: {"name": "thumbnailImageHash", "type": -6, "array": False, "value": 5},
                6: {"name": "faviconImageHash", "type": -6, "array": False, "value": 6},
                7: {"name": "thumbnailImageWidth", "type": -5, "array": False, "value": 7},
                8: {"name": "thumbnailImageHeight", "type": -5, "array": False, "value": 8},
            }
        ),
    },
    {
        "name": "Viewport",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "canvasSpaceBounds", "type": 50, "array": False, "value": 1},
                2: {"name": "pixelPreview", "type": -1, "array": False, "value": 2},
                3: {"name": "pixelDensity", "type": -5, "array": False, "value": 3},
                4: {"name": "canvasGuid", "type": 47, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "Mouse",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "cursor", "type": 22, "array": False, "value": 1},
                2: {"name": "canvasSpaceLocation", "type": 49, "array": False, "value": 2},
                3: {"name": "canvasSpaceSelectionBox", "type": 50, "array": False, "value": 3},
                4: {"name": "canvasGuid", "type": 47, "array": False, "value": 4},
                5: {"name": "cursorHiddenReason", "type": -4, "array": False, "value": 5},
            }
        ),
    },
    {
        "name": "Click",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "id", "type": -4, "array": False, "value": 1},
                2: {"name": "point", "type": 49, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ScrollPosition",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "node", "type": 47, "array": False, "value": 1},
                2: {"name": "scrollOffset", "type": 49, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "TriggeredOverlay",
        "kind": 1,
        "fields": OrderedDict(
            {
                1: {"name": "overlayGuid", "type": 47, "array": False, "value": 1},
                2: {"name": "hotspotGuid", "type": 47, "array": False, "value": 2},
                3: {"name": "swapGuid", "type": 47, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "TriggeredOverlayData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "overlayGuid", "type": 47, "array": False, "value": 1},
                2: {"name": "hotspotGuid", "type": 47, "array": False, "value": 2},
                3: {"name": "swapGuid", "type": 47, "array": False, "value": 3},
                4: {"name": "prototypeInteractionGuid", "type": 47, "array": False, "value": 4},
                5: {"name": "hotspotBlueprintId", "type": 84, "array": False, "value": 5},
            }
        ),
    },
    {
        "name": "TriggeredSetVariableActionData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {
                    "name": "nodeForFindingTopmostScreenId",
                    "type": 47,
                    "array": False,
                    "value": 1,
                },
                2: {"name": "targetVariableId", "type": -6, "array": False, "value": 2},
                3: {"name": "targetVariableData", "type": -6, "array": False, "value": 3},
                4: {"name": "resolvedVariableModes", "type": -6, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "VideoStateChangeData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "targetNodeId", "type": 47, "array": False, "value": 1},
                2: {"name": "isPlaying", "type": -1, "array": False, "value": 2},
                3: {"name": "isPlayingSound", "type": -1, "array": False, "value": 3},
                4: {"name": "currentTimes", "type": -4, "array": True, "value": 4},
                5: {"name": "actionTakenTimestamp", "type": -4, "array": False, "value": 5},
            }
        ),
    },
    {
        "name": "PresentedState",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "baseScreenID", "type": 47, "array": False, "value": 1},
                2: {"name": "overlays", "type": 228, "array": True, "value": 2},
            }
        ),
    },
    {
        "name": "TransitionDirection",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "FORWARD", "type": 0, "array": False, "value": 0},
                1: {"name": "REVERSE", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "TopLevelPlaybackChange",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "oldState", "type": 231, "array": False, "value": 1},
                2: {"name": "newState", "type": 231, "array": False, "value": 2},
                3: {"name": "hotspotBlueprintID", "type": 84, "array": False, "value": 3},
                4: {"name": "interactionID", "type": 47, "array": False, "value": 4},
                5: {
                    "name": "isHotspotInNewPresentedState",
                    "type": -1,
                    "array": False,
                    "value": 5,
                },
                6: {"name": "direction", "type": 232, "array": False, "value": 6},
                7: {"name": "instanceStablePath", "type": 84, "array": False, "value": 7},
            }
        ),
    },
    {
        "name": "InstanceStateChange",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "stateID", "type": 47, "array": False, "value": 1},
                2: {"name": "interactionID", "type": 47, "array": False, "value": 2},
                3: {"name": "hotspotStablePath", "type": 84, "array": False, "value": 3},
                4: {"name": "instanceStablePath", "type": 84, "array": False, "value": 4},
                5: {"name": "phase", "type": 237, "array": False, "value": 5},
            }
        ),
    },
    {
        "name": "TextCursor",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "selectionBox", "type": 50, "array": False, "value": 1},
                2: {"name": "canvasGuid", "type": 47, "array": False, "value": 2},
                3: {"name": "textNodeGuid", "type": 47, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "TextSelection",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "selectionBoxes", "type": 50, "array": True, "value": 1},
                2: {"name": "canvasGuid", "type": 47, "array": False, "value": 2},
                3: {"name": "textNodeGuid", "type": 47, "array": False, "value": 3},
                4: {"name": "textSelectionRange", "type": 49, "array": False, "value": 4},
                5: {"name": "textNodeOrContainingIfGuid", "type": 47, "array": False, "value": 5},
                6: {"name": "tableCellRowId", "type": 47, "array": False, "value": 6},
                7: {"name": "tableCellColId", "type": 47, "array": False, "value": 7},
            }
        ),
    },
    {
        "name": "PlaybackChangePhase",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "INITIATED", "type": 0, "array": False, "value": 0},
                1: {"name": "ABORTED", "type": 0, "array": False, "value": 1},
                2: {"name": "COMMITTED", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "PlaybackChangeKeyframe",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "phase", "type": 237, "array": False, "value": 1},
                2: {"name": "progress", "type": -5, "array": False, "value": 2},
                3: {"name": "timestamp", "type": -5, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "StateMapping",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "stablePath", "type": 84, "array": False, "value": 1},
                2: {"name": "lastTopLevelChange", "type": 233, "array": False, "value": 2},
                3: {"name": "lastTopLevelChangeStatus", "type": 238, "array": False, "value": 3},
                4: {"name": "timestamp", "type": -5, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "ScrollMapping",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "blueprintID", "type": 84, "array": False, "value": 1},
                2: {"name": "overlayIndex", "type": -4, "array": False, "value": 2},
                3: {"name": "scrollOffset", "type": 49, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "PlaybackUpdate",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "lastTopLevelChange", "type": 233, "array": False, "value": 1},
                2: {"name": "lastTopLevelChangeStatus", "type": 238, "array": False, "value": 2},
                3: {"name": "scrollMappings", "type": 240, "array": True, "value": 3},
                4: {"name": "timestamp", "type": -5, "array": False, "value": 4},
                5: {"name": "pointerLocation", "type": 49, "array": False, "value": 5},
                6: {"name": "isTopLevelFrameChange", "type": -1, "array": False, "value": 6},
                7: {"name": "stateMappings", "type": 239, "array": True, "value": 7},
            }
        ),
    },
    {
        "name": "ChatMessage",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "text", "type": -6, "array": False, "value": 1},
                2: {"name": "previousText", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "VoiceMetadata",
        "kind": 2,
        "fields": OrderedDict(
            {1: {"name": "connectedCallId", "type": -6, "array": False, "value": 1}}
        ),
    },
    {
        "name": "Heartbeat",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "FOREGROUND", "type": 0, "array": False, "value": 0},
                1: {"name": "BACKGROUND", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "UserChange",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "sessionID", "type": -4, "array": False, "value": 1},
                2: {"name": "connected", "type": -1, "array": False, "value": 2},
                3: {"name": "name", "type": -6, "array": False, "value": 3},
                4: {"name": "color", "type": 48, "array": False, "value": 4},
                5: {"name": "imageURL", "type": -6, "array": False, "value": 5},
                6: {"name": "viewport", "type": 223, "array": False, "value": 6},
                7: {"name": "mouse", "type": 224, "array": False, "value": 7},
                8: {"name": "selection", "type": 47, "array": True, "value": 8},
                9: {"name": "observing", "type": -4, "array": True, "value": 9},
                10: {"name": "deviceName", "type": -6, "array": False, "value": 10},
                11: {"name": "recentClicks", "type": 225, "array": True, "value": 11},
                12: {"name": "scrollPositions", "type": 226, "array": True, "value": 12},
                13: {"name": "triggeredOverlays", "type": 227, "array": True, "value": 13},
                14: {"name": "userID", "type": -6, "array": False, "value": 14},
                15: {"name": "lastTriggeredHotspot", "type": 47, "array": False, "value": 15},
                16: {
                    "name": "lastTriggeredPrototypeInteractionID",
                    "type": 47,
                    "array": False,
                    "value": 16,
                },
                17: {"name": "triggeredOverlaysData", "type": 228, "array": True, "value": 17},
                18: {"name": "playbackUpdates", "type": 241, "array": True, "value": 18},
                19: {"name": "chatMessage", "type": 242, "array": False, "value": 19},
                20: {"name": "voiceMetadata", "type": 243, "array": False, "value": 20},
                21: {"name": "canWrite", "type": -1, "array": False, "value": 21},
                22: {"name": "highFiveStatus", "type": -1, "array": False, "value": 22},
                23: {"name": "instanceStateChanges", "type": 234, "array": True, "value": 23},
                24: {"name": "textCursor", "type": 235, "array": False, "value": 24},
                25: {"name": "textSelection", "type": 236, "array": False, "value": 25},
                26: {"name": "connectedAtTimeS", "type": -4, "array": False, "value": 26},
                27: {"name": "focusOnTextCursor", "type": -1, "array": False, "value": 27},
                28: {"name": "heartbeat", "type": 244, "array": False, "value": 28},
                29: {
                    "name": "triggeredSetVariableActionData",
                    "type": 229,
                    "array": True,
                    "value": 29,
                },
                30: {"name": "videoStateChangeData", "type": 230, "array": True, "value": 30},
            }
        ),
    },
    {
        "name": "InteractiveSlideElementChange",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "userID", "type": -6, "array": False, "value": 1},
                2: {"name": "anonymousUserID", "type": -6, "array": False, "value": 2},
                3: {"name": "nodeID", "type": 47, "array": False, "value": 3},
                4: {"name": "responseData", "type": -6, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "SceneGraphQueryBehavior",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "DEFAULT", "type": 0, "array": False, "value": 0},
                1: {"name": "CONTAINING_PAGE", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "SceneGraphQuery",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "startingNode", "type": 47, "array": False, "value": 1},
                2: {"name": "depth", "type": -4, "array": False, "value": 2},
                3: {"name": "behavior", "type": 247, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "NodeChangesMetadata",
        "kind": 2,
        "fields": OrderedDict(
            {1: {"name": "blobsFieldOffset", "type": -4, "array": False, "value": 1}}
        ),
    },
    {
        "name": "CursorReaction",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "imageUrl", "type": -6, "array": False, "value": 1}}),
    },
    {
        "name": "TimerInfo",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "isPaused", "type": -1, "array": False, "value": 1},
                2: {"name": "timeRemainingMs", "type": -4, "array": False, "value": 2},
                3: {"name": "totalTimeMs", "type": -4, "array": False, "value": 3},
                4: {"name": "timerID", "type": -4, "array": False, "value": 4},
                5: {"name": "setBy", "type": -6, "array": False, "value": 5},
                6: {"name": "songID", "type": -4, "array": False, "value": 6},
                7: {"name": "lastReceivedSongTimestampMs", "type": -4, "array": False, "value": 7},
                8: {"name": "songUUID", "type": -6, "array": False, "value": 8},
            }
        ),
    },
    {
        "name": "MusicInfo",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "isPaused", "type": -1, "array": False, "value": 1},
                2: {"name": "messageID", "type": -4, "array": False, "value": 2},
                3: {"name": "songID", "type": -6, "array": False, "value": 3},
                4: {"name": "lastReceivedSongTimestampMs", "type": -4, "array": False, "value": 4},
                5: {"name": "isStopped", "type": -1, "array": False, "value": 5},
            }
        ),
    },
    {
        "name": "PresenterNomination",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "sessionID", "type": -4, "array": False, "value": 1},
                2: {"name": "isCancelled", "type": -1, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "PresenterInfo",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "sessionID", "type": -4, "array": False, "value": 1},
                2: {"name": "nomination", "type": 253, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ClientBroadcast",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "sessionID", "type": -4, "array": False, "value": 1},
                2: {"name": "cursorReaction", "type": 250, "array": False, "value": 2},
                3: {"name": "timer", "type": 251, "array": False, "value": 3},
                4: {"name": "presenter", "type": 254, "array": False, "value": 4},
                5: {"name": "prototypePresenter", "type": 254, "array": False, "value": 5},
                6: {"name": "music", "type": 252, "array": False, "value": 6},
            }
        ),
    },
    {
        "name": "Message",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "type", "type": 0, "array": False, "value": 1},
                2: {"name": "sessionID", "type": -4, "array": False, "value": 2},
                3: {"name": "ackID", "type": -4, "array": False, "value": 3},
                4: {"name": "nodeChanges", "type": 152, "array": True, "value": 4},
                5: {"name": "userChanges", "type": 245, "array": True, "value": 5},
                32: {
                    "name": "interactiveSlideElementChange",
                    "type": 246,
                    "array": False,
                    "value": 32,
                },
                6: {"name": "blobs", "type": 67, "array": True, "value": 6},
                30: {"name": "blobBaseIndex", "type": -4, "array": False, "value": 30},
                7: {"name": "signalName", "type": -6, "array": False, "value": 7},
                8: {"name": "access", "type": 2, "array": False, "value": 8},
                9: {"name": "styleSetName", "type": -6, "array": False, "value": 9},
                10: {"name": "styleSetType", "type": 31, "array": False, "value": 10},
                11: {"name": "styleSetContentType", "type": 32, "array": False, "value": 11},
                12: {"name": "pasteID", "type": -3, "array": False, "value": 12},
                13: {"name": "pasteOffset", "type": 49, "array": False, "value": 13},
                14: {"name": "pasteFileKey", "type": -6, "array": False, "value": 14},
                15: {"name": "signalPayload", "type": -6, "array": False, "value": 15},
                16: {"name": "sceneGraphQueries", "type": 248, "array": True, "value": 16},
                17: {"name": "nodeChangesMetadata", "type": 249, "array": False, "value": 17},
                18: {"name": "fileVersion", "type": -4, "array": False, "value": 18},
                19: {
                    "name": "pasteIsPartiallyOutsideEnclosingFrame",
                    "type": -1,
                    "array": False,
                    "value": 19,
                },
                20: {"name": "pastePageId", "type": 47, "array": False, "value": 20},
                21: {"name": "isCut", "type": -1, "array": False, "value": 21},
                22: {"name": "localUndoStack", "type": 256, "array": True, "value": 22},
                23: {"name": "localRedoStack", "type": 256, "array": True, "value": 23},
                24: {"name": "broadcasts", "type": 255, "array": True, "value": 24},
                25: {"name": "reconnectSequenceNumber", "type": -4, "array": False, "value": 25},
                26: {"name": "pasteBranchSourceFileKey", "type": -6, "array": False, "value": 26},
                27: {"name": "pasteEditorType", "type": 147, "array": False, "value": 27},
                28: {"name": "postSyncActions", "type": -6, "array": False, "value": 28},
                29: {"name": "publishedAssetGuids", "type": 47, "array": True, "value": 29},
                31: {"name": "dirtyFromInitialLoad", "type": -1, "array": False, "value": 31},
            }
        ),
    },
    {
        "name": "DiffChunk",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "nodeChanges", "type": -4, "array": True, "value": 1},
                2: {"name": "phase", "type": 3, "array": False, "value": 2},
                3: {"name": "displayNode", "type": 152, "array": False, "value": 3},
                4: {"name": "canvasId", "type": 47, "array": False, "value": 4},
                5: {"name": "canvasName", "type": -6, "array": False, "value": 5},
                6: {"name": "canvasIsInternal", "type": -1, "array": False, "value": 6},
                7: {"name": "chunksAffectingThisChunk", "type": -4, "array": True, "value": 7},
                8: {"name": "basisParentHierarchy", "type": 152, "array": True, "value": 8},
                9: {"name": "parentHierarchy", "type": 152, "array": True, "value": 9},
                10: {"name": "basisParentHierarchyGuids", "type": 47, "array": True, "value": 10},
                11: {"name": "parentHierarchyGuids", "type": 47, "array": True, "value": 11},
            }
        ),
    },
    {
        "name": "DiffPayload",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "nodeChanges", "type": 152, "array": True, "value": 1},
                2: {"name": "blobs", "type": 67, "array": True, "value": 2},
                3: {"name": "diffChunks", "type": 257, "array": True, "value": 3},
                4: {"name": "diffBasis", "type": 152, "array": True, "value": 4},
                5: {"name": "basisParentNodeChanges", "type": 152, "array": True, "value": 5},
                6: {"name": "parentNodeChanges", "type": 152, "array": True, "value": 6},
            }
        ),
    },
    {
        "name": "RichMediaType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "ANIMATED_IMAGE", "type": 0, "array": False, "value": 0},
                1: {"name": "VIDEO", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "RichMediaData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "mediaHash", "type": -6, "array": False, "value": 1},
                2: {"name": "richMediaType", "type": 259, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "VariableDataType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "BOOLEAN", "type": 0, "array": False, "value": 0},
                1: {"name": "FLOAT", "type": 0, "array": False, "value": 1},
                2: {"name": "STRING", "type": 0, "array": False, "value": 2},
                3: {"name": "ALIAS", "type": 0, "array": False, "value": 3},
                4: {"name": "COLOR", "type": 0, "array": False, "value": 4},
                5: {"name": "EXPRESSION", "type": 0, "array": False, "value": 5},
                6: {"name": "MAP", "type": 0, "array": False, "value": 6},
                7: {"name": "SYMBOL_ID", "type": 0, "array": False, "value": 7},
                8: {"name": "FONT_STYLE", "type": 0, "array": False, "value": 8},
            }
        ),
    },
    {
        "name": "VariableResolvedDataType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "BOOLEAN", "type": 0, "array": False, "value": 0},
                1: {"name": "FLOAT", "type": 0, "array": False, "value": 1},
                2: {"name": "STRING", "type": 0, "array": False, "value": 2},
                4: {"name": "COLOR", "type": 0, "array": False, "value": 4},
                5: {"name": "MAP", "type": 0, "array": False, "value": 5},
                6: {"name": "SYMBOL_ID", "type": 0, "array": False, "value": 6},
            }
        ),
    },
    {
        "name": "VariableAnyValue",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "boolValue", "type": -1, "array": False, "value": 1},
                2: {"name": "textValue", "type": -6, "array": False, "value": 2},
                3: {"name": "floatValue", "type": -5, "array": False, "value": 3},
                4: {"name": "alias", "type": 96, "array": False, "value": 4},
                5: {"name": "colorValue", "type": 48, "array": False, "value": 5},
                6: {"name": "expressionValue", "type": 265, "array": False, "value": 6},
                7: {"name": "mapValue", "type": 267, "array": False, "value": 7},
                8: {"name": "symbolIdValue", "type": 95, "array": False, "value": 8},
                9: {"name": "fontStyleValue", "type": 268, "array": False, "value": 9},
            }
        ),
    },
    {
        "name": "ExpressionFunction",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "ADDITION", "type": 0, "array": False, "value": 0},
                1: {"name": "SUBTRACTION", "type": 0, "array": False, "value": 1},
                2: {"name": "RESOLVE_VARIANT", "type": 0, "array": False, "value": 2},
                3: {"name": "MULTIPLY", "type": 0, "array": False, "value": 3},
                4: {"name": "DIVIDE", "type": 0, "array": False, "value": 4},
                5: {"name": "EQUALS", "type": 0, "array": False, "value": 5},
                6: {"name": "NOT_EQUAL", "type": 0, "array": False, "value": 6},
                7: {"name": "LESS_THAN", "type": 0, "array": False, "value": 7},
                8: {"name": "LESS_THAN_OR_EQUAL", "type": 0, "array": False, "value": 8},
                9: {"name": "GREATER_THAN", "type": 0, "array": False, "value": 9},
                10: {"name": "GREATER_THAN_OR_EQUAL", "type": 0, "array": False, "value": 10},
                11: {"name": "AND", "type": 0, "array": False, "value": 11},
                12: {"name": "OR", "type": 0, "array": False, "value": 12},
                13: {"name": "NOT", "type": 0, "array": False, "value": 13},
                14: {"name": "STRINGIFY", "type": 0, "array": False, "value": 14},
                15: {"name": "TERNARY", "type": 0, "array": False, "value": 15},
                16: {"name": "VAR_MODE_LOOKUP", "type": 0, "array": False, "value": 16},
                17: {"name": "NEGATE", "type": 0, "array": False, "value": 17},
            }
        ),
    },
    {
        "name": "Expression",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "expressionFunction", "type": 264, "array": False, "value": 1},
                2: {"name": "expressionArguments", "type": 269, "array": True, "value": 2},
            }
        ),
    },
    {
        "name": "VariableMapValue",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "key", "type": -6, "array": False, "value": 1},
                2: {"name": "value", "type": 269, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "VariableMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "values", "type": 266, "array": True, "value": 1}}),
    },
    {
        "name": "VariableFontStyle",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "asString", "type": 269, "array": False, "value": 1},
                2: {"name": "asFloat", "type": 269, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "VariableData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "value", "type": 263, "array": False, "value": 1},
                2: {"name": "dataType", "type": 261, "array": False, "value": 2},
                3: {"name": "resolvedDataType", "type": 262, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "VariableSetMode",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "id", "type": 47, "array": False, "value": 1},
                2: {"name": "name", "type": -6, "array": False, "value": 2},
                3: {"name": "sortPosition", "type": -6, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "VariableDataValues",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 272, "array": True, "value": 1}}),
    },
    {
        "name": "VariableDataValuesEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "modeID", "type": 47, "array": False, "value": 1},
                2: {"name": "variableData", "type": 269, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "VariableScope",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "ALL_SCOPES", "type": 0, "array": False, "value": 0},
                1: {"name": "TEXT_CONTENT", "type": 0, "array": False, "value": 1},
                2: {"name": "CORNER_RADIUS", "type": 0, "array": False, "value": 2},
                3: {"name": "WIDTH_HEIGHT", "type": 0, "array": False, "value": 3},
                4: {"name": "GAP", "type": 0, "array": False, "value": 4},
                5: {"name": "ALL_FILLS", "type": 0, "array": False, "value": 5},
                6: {"name": "FRAME_FILL", "type": 0, "array": False, "value": 6},
                7: {"name": "SHAPE_FILL", "type": 0, "array": False, "value": 7},
                8: {"name": "TEXT_FILL", "type": 0, "array": False, "value": 8},
                9: {"name": "STROKE", "type": 0, "array": False, "value": 9},
            }
        ),
    },
    {
        "name": "CodeSyntaxPlatform",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "WEB", "type": 0, "array": False, "value": 0},
                1: {"name": "ANDROID", "type": 0, "array": False, "value": 1},
                2: {"name": "iOS", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "OptionalVector",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "value", "type": 49, "array": False, "value": 1}}),
    },
    {
        "name": "HTMLTag",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "AUTO", "type": 0, "array": False, "value": 0},
                1: {"name": "ARTICLE", "type": 0, "array": False, "value": 1},
                2: {"name": "SECTION", "type": 0, "array": False, "value": 2},
                3: {"name": "NAV", "type": 0, "array": False, "value": 3},
                4: {"name": "ASIDE", "type": 0, "array": False, "value": 4},
                5: {"name": "H1", "type": 0, "array": False, "value": 5},
                6: {"name": "H2", "type": 0, "array": False, "value": 6},
                7: {"name": "H3", "type": 0, "array": False, "value": 7},
                8: {"name": "H4", "type": 0, "array": False, "value": 8},
                9: {"name": "H5", "type": 0, "array": False, "value": 9},
                10: {"name": "H6", "type": 0, "array": False, "value": 10},
                11: {"name": "HGROUP", "type": 0, "array": False, "value": 11},
                12: {"name": "HEADER", "type": 0, "array": False, "value": 12},
                13: {"name": "FOOTER", "type": 0, "array": False, "value": 13},
                14: {"name": "ADDRESS", "type": 0, "array": False, "value": 14},
                15: {"name": "P", "type": 0, "array": False, "value": 15},
                16: {"name": "HR", "type": 0, "array": False, "value": 16},
                17: {"name": "PRE", "type": 0, "array": False, "value": 17},
                18: {"name": "BLOCKQUOTE", "type": 0, "array": False, "value": 18},
                19: {"name": "OL", "type": 0, "array": False, "value": 19},
                20: {"name": "UL", "type": 0, "array": False, "value": 20},
                21: {"name": "MENU", "type": 0, "array": False, "value": 21},
                22: {"name": "LI", "type": 0, "array": False, "value": 22},
                23: {"name": "DL", "type": 0, "array": False, "value": 23},
                24: {"name": "DT", "type": 0, "array": False, "value": 24},
                25: {"name": "DD", "type": 0, "array": False, "value": 25},
                26: {"name": "FIGURE", "type": 0, "array": False, "value": 26},
                27: {"name": "FIGCAPTION", "type": 0, "array": False, "value": 27},
                28: {"name": "MAIN", "type": 0, "array": False, "value": 28},
                29: {"name": "DIV", "type": 0, "array": False, "value": 29},
                30: {"name": "A", "type": 0, "array": False, "value": 30},
                31: {"name": "EM", "type": 0, "array": False, "value": 31},
                32: {"name": "STRONG", "type": 0, "array": False, "value": 32},
                33: {"name": "SMALL", "type": 0, "array": False, "value": 33},
                34: {"name": "S", "type": 0, "array": False, "value": 34},
                35: {"name": "CITE", "type": 0, "array": False, "value": 35},
                36: {"name": "Q", "type": 0, "array": False, "value": 36},
                37: {"name": "DFN", "type": 0, "array": False, "value": 37},
                38: {"name": "ABBR", "type": 0, "array": False, "value": 38},
                39: {"name": "RUBY", "type": 0, "array": False, "value": 39},
                40: {"name": "RT", "type": 0, "array": False, "value": 40},
                41: {"name": "RP", "type": 0, "array": False, "value": 41},
                42: {"name": "DATA", "type": 0, "array": False, "value": 42},
                43: {"name": "TIME", "type": 0, "array": False, "value": 43},
                44: {"name": "CODE", "type": 0, "array": False, "value": 44},
                45: {"name": "VAR", "type": 0, "array": False, "value": 45},
                46: {"name": "SAMP", "type": 0, "array": False, "value": 46},
                47: {"name": "KBD", "type": 0, "array": False, "value": 47},
                48: {"name": "SUB", "type": 0, "array": False, "value": 48},
                49: {"name": "SUP", "type": 0, "array": False, "value": 49},
                50: {"name": "I", "type": 0, "array": False, "value": 50},
                51: {"name": "B", "type": 0, "array": False, "value": 51},
                52: {"name": "U", "type": 0, "array": False, "value": 52},
                53: {"name": "MARK", "type": 0, "array": False, "value": 53},
                54: {"name": "BDI", "type": 0, "array": False, "value": 54},
                55: {"name": "BDO", "type": 0, "array": False, "value": 55},
                56: {"name": "SPAN", "type": 0, "array": False, "value": 56},
                57: {"name": "BR", "type": 0, "array": False, "value": 57},
                58: {"name": "WBR", "type": 0, "array": False, "value": 58},
                59: {"name": "PICTURE", "type": 0, "array": False, "value": 59},
                60: {"name": "SOURCE", "type": 0, "array": False, "value": 60},
                61: {"name": "IMG", "type": 0, "array": False, "value": 61},
                62: {"name": "FORM", "type": 0, "array": False, "value": 62},
                63: {"name": "LABEL", "type": 0, "array": False, "value": 63},
                64: {"name": "INPUT", "type": 0, "array": False, "value": 64},
                65: {"name": "BUTTON", "type": 0, "array": False, "value": 65},
                66: {"name": "SELECT", "type": 0, "array": False, "value": 66},
                67: {"name": "DATALIST", "type": 0, "array": False, "value": 67},
                68: {"name": "OPTGROUP", "type": 0, "array": False, "value": 68},
                69: {"name": "OPTION", "type": 0, "array": False, "value": 69},
                70: {"name": "TEXTAREA", "type": 0, "array": False, "value": 70},
                71: {"name": "OUTPUT", "type": 0, "array": False, "value": 71},
                72: {"name": "PROGRESS", "type": 0, "array": False, "value": 72},
                73: {"name": "METER", "type": 0, "array": False, "value": 73},
                74: {"name": "FIELDSET", "type": 0, "array": False, "value": 74},
                75: {"name": "LEGEND", "type": 0, "array": False, "value": 75},
            }
        ),
    },
    {
        "name": "ARIARole",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "AUTO", "type": 0, "array": False, "value": 0},
                52: {"name": "NONE", "type": 0, "array": False, "value": 52},
                30: {"name": "APPLICATION", "type": 0, "array": False, "value": 30},
                67: {"name": "BANNER", "type": 0, "array": False, "value": 67},
                68: {"name": "COMPLEMENTARY", "type": 0, "array": False, "value": 68},
                69: {"name": "CONTENTINFO", "type": 0, "array": False, "value": 69},
                70: {"name": "FORM", "type": 0, "array": False, "value": 70},
                71: {"name": "MAIN", "type": 0, "array": False, "value": 71},
                72: {"name": "NAVIGATION", "type": 0, "array": False, "value": 72},
                73: {"name": "REGION", "type": 0, "array": False, "value": 73},
                74: {"name": "SEARCH", "type": 0, "array": False, "value": 74},
                13: {"name": "SEPARATOR", "type": 0, "array": False, "value": 13},
                31: {"name": "ARTICLE", "type": 0, "array": False, "value": 31},
                35: {"name": "COLUMNHEADER", "type": 0, "array": False, "value": 35},
                36: {"name": "DEFINITION", "type": 0, "array": False, "value": 36},
                38: {"name": "DIRECTORY", "type": 0, "array": False, "value": 38},
                39: {"name": "DOCUMENT", "type": 0, "array": False, "value": 39},
                44: {"name": "GROUP", "type": 0, "array": False, "value": 44},
                45: {"name": "HEADING", "type": 0, "array": False, "value": 45},
                46: {"name": "IMG", "type": 0, "array": False, "value": 46},
                48: {"name": "LIST", "type": 0, "array": False, "value": 48},
                49: {"name": "LISTITEM", "type": 0, "array": False, "value": 49},
                50: {"name": "MATH", "type": 0, "array": False, "value": 50},
                53: {"name": "NOTE", "type": 0, "array": False, "value": 53},
                55: {"name": "PRESENTATION", "type": 0, "array": False, "value": 55},
                56: {"name": "ROW", "type": 0, "array": False, "value": 56},
                57: {"name": "ROWGROUP", "type": 0, "array": False, "value": 57},
                58: {"name": "ROWHEADER", "type": 0, "array": False, "value": 58},
                62: {"name": "TABLE", "type": 0, "array": False, "value": 62},
                65: {"name": "TOOLBAR", "type": 0, "array": False, "value": 65},
                1: {"name": "BUTTON", "type": 0, "array": False, "value": 1},
                2: {"name": "CHECKBOX", "type": 0, "array": False, "value": 2},
                3: {"name": "GRIDCELL", "type": 0, "array": False, "value": 3},
                4: {"name": "LINK", "type": 0, "array": False, "value": 4},
                5: {"name": "MENUITEM", "type": 0, "array": False, "value": 5},
                6: {"name": "MENUITEMCHECKBOX", "type": 0, "array": False, "value": 6},
                7: {"name": "MENUITEMRADIO", "type": 0, "array": False, "value": 7},
                8: {"name": "OPTION", "type": 0, "array": False, "value": 8},
                9: {"name": "PROGRESSBAR", "type": 0, "array": False, "value": 9},
                10: {"name": "RADIO", "type": 0, "array": False, "value": 10},
                11: {"name": "SCROLLBAR", "type": 0, "array": False, "value": 11},
                14: {"name": "SLIDER", "type": 0, "array": False, "value": 14},
                15: {"name": "SPINBUTTON", "type": 0, "array": False, "value": 15},
                17: {"name": "TAB", "type": 0, "array": False, "value": 17},
                18: {"name": "TABPANEL", "type": 0, "array": False, "value": 18},
                19: {"name": "TEXTBOX", "type": 0, "array": False, "value": 19},
                20: {"name": "TREEITEM", "type": 0, "array": False, "value": 20},
                21: {"name": "COMBOBOX", "type": 0, "array": False, "value": 21},
                22: {"name": "GRID", "type": 0, "array": False, "value": 22},
                23: {"name": "LISTBOX", "type": 0, "array": False, "value": 23},
                24: {"name": "MENU", "type": 0, "array": False, "value": 24},
                25: {"name": "MENUBAR", "type": 0, "array": False, "value": 25},
                26: {"name": "RADIOGROUP", "type": 0, "array": False, "value": 26},
                27: {"name": "TABLIST", "type": 0, "array": False, "value": 27},
                28: {"name": "TREE", "type": 0, "array": False, "value": 28},
                29: {"name": "TREEGRID", "type": 0, "array": False, "value": 29},
                66: {"name": "TOOLTIP", "type": 0, "array": False, "value": 66},
                75: {"name": "ALERT", "type": 0, "array": False, "value": 75},
                76: {"name": "LOG", "type": 0, "array": False, "value": 76},
                77: {"name": "MARQUEE", "type": 0, "array": False, "value": 77},
                78: {"name": "STATUS", "type": 0, "array": False, "value": 78},
                79: {"name": "TIMER", "type": 0, "array": False, "value": 79},
                80: {"name": "ALERTDIALOG", "type": 0, "array": False, "value": 80},
                81: {"name": "DIALOG", "type": 0, "array": False, "value": 81},
                12: {"name": "SEARCHBOX", "type": 0, "array": False, "value": 12},
                16: {"name": "SWITCH", "type": 0, "array": False, "value": 16},
                32: {"name": "BLOCKQUOTE", "type": 0, "array": False, "value": 32},
                33: {"name": "CAPTION", "type": 0, "array": False, "value": 33},
                34: {"name": "CELL", "type": 0, "array": False, "value": 34},
                37: {"name": "DELETION", "type": 0, "array": False, "value": 37},
                40: {"name": "EMPHASIS", "type": 0, "array": False, "value": 40},
                41: {"name": "FEED", "type": 0, "array": False, "value": 41},
                42: {"name": "FIGURE", "type": 0, "array": False, "value": 42},
                43: {"name": "GENERIC", "type": 0, "array": False, "value": 43},
                47: {"name": "INSERTION", "type": 0, "array": False, "value": 47},
                51: {"name": "METER", "type": 0, "array": False, "value": 51},
                54: {"name": "PARAGRAPH", "type": 0, "array": False, "value": 54},
                59: {"name": "STRONG", "type": 0, "array": False, "value": 59},
                60: {"name": "SUBSCRIPT", "type": 0, "array": False, "value": 60},
                61: {"name": "SUPERSCRIPT", "type": 0, "array": False, "value": 61},
                63: {"name": "TERM", "type": 0, "array": False, "value": 63},
                64: {"name": "TIME", "type": 0, "array": False, "value": 64},
                82: {"name": "IMAGE", "type": 0, "array": False, "value": 82},
                83: {"name": "HEADING_1", "type": 0, "array": False, "value": 83},
                84: {"name": "HEADING_2", "type": 0, "array": False, "value": 84},
                85: {"name": "HEADING_3", "type": 0, "array": False, "value": 85},
                86: {"name": "HEADING_4", "type": 0, "array": False, "value": 86},
                87: {"name": "HEADING_5", "type": 0, "array": False, "value": 87},
                88: {"name": "HEADING_6", "type": 0, "array": False, "value": 88},
                89: {"name": "HEADER", "type": 0, "array": False, "value": 89},
                90: {"name": "FOOTER", "type": 0, "array": False, "value": 90},
                91: {"name": "SIDEBAR", "type": 0, "array": False, "value": 91},
                92: {"name": "SECTION", "type": 0, "array": False, "value": 92},
                93: {"name": "MAINCONTENT", "type": 0, "array": False, "value": 93},
                94: {"name": "TABLE_CELL", "type": 0, "array": False, "value": 94},
                95: {"name": "WIDGET", "type": 0, "array": False, "value": 95},
            }
        ),
    },
    {
        "name": "MigrationStatus",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "dsdCleanup", "type": -1, "array": False, "value": 1}}),
    },
    {
        "name": "NodeFieldMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 280, "array": True, "value": 1}}),
    },
    {
        "name": "NodeFieldMapEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                2: {"name": "field", "type": -4, "array": False, "value": 2},
                3: {"name": "lastModifiedSequenceNumber", "type": -4, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "ColorProfile",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "SRGB", "type": 0, "array": False, "value": 0},
                1: {"name": "DISPLAY_P3", "type": 0, "array": False, "value": 1},
            }
        ),
    },
    {
        "name": "DocumentColorProfile",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "LEGACY", "type": 0, "array": False, "value": 0},
                1: {"name": "SRGB", "type": 0, "array": False, "value": 1},
                2: {"name": "DISPLAY_P3", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ChildReadingDirection",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "NONE", "type": 0, "array": False, "value": 0},
                1: {"name": "LEFT_TO_RIGHT", "type": 0, "array": False, "value": 1},
                2: {"name": "RIGHT_TO_LEFT", "type": 0, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ARIAAttributeAnyValue",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "boolValue", "type": -1, "array": False, "value": 1},
                2: {"name": "stringValue", "type": -6, "array": False, "value": 2},
                3: {"name": "floatValue", "type": -5, "array": False, "value": 3},
                4: {"name": "intValue", "type": -3, "array": False, "value": 4},
                5: {"name": "stringArrayValue", "type": -6, "array": True, "value": 5},
            }
        ),
    },
    {
        "name": "ARIAAttributeDataType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "BOOLEAN", "type": 0, "array": False, "value": 0},
                1: {"name": "STRING", "type": 0, "array": False, "value": 1},
                2: {"name": "FLOAT", "type": 0, "array": False, "value": 2},
                3: {"name": "INT", "type": 0, "array": False, "value": 3},
                4: {"name": "STRING_LIST", "type": 0, "array": False, "value": 4},
            }
        ),
    },
    {
        "name": "ARIAAttributeData",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "type", "type": 285, "array": False, "value": 1},
                2: {"name": "value", "type": 284, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "ARIAAttributesMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 288, "array": True, "value": 1}}),
    },
    {
        "name": "ARIAAttributesMapEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "attribute", "type": -6, "array": False, "value": 1},
                2: {"name": "value", "type": 286, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "HandoffStatusMapEntry",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "guid", "type": 47, "array": False, "value": 1},
                2: {"name": "handoffStatus", "type": 151, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "HandoffStatusMap",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "entries", "type": 289, "array": True, "value": 1}}),
    },
    {
        "name": "EditScopeInfo",
        "kind": 2,
        "fields": OrderedDict(
            {1: {"name": "editScopeStacks", "type": 292, "array": True, "value": 1}}
        ),
    },
    {
        "name": "EditScopeStack",
        "kind": 2,
        "fields": OrderedDict({1: {"name": "stack", "type": 293, "array": True, "value": 1}}),
    },
    {
        "name": "EditScope",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "type", "type": 294, "array": False, "value": 1},
                2: {"name": "label", "type": -6, "array": False, "value": 2},
            }
        ),
    },
    {
        "name": "EditScopeType",
        "kind": 0,
        "fields": OrderedDict(
            {
                0: {"name": "INVALID", "type": 0, "array": False, "value": 0},
                1: {"name": "TEST_SETUP", "type": 0, "array": False, "value": 1},
                2: {"name": "USER", "type": 0, "array": False, "value": 2},
                3: {"name": "PLUGIN", "type": 0, "array": False, "value": 3},
                4: {"name": "SYSTEM", "type": 0, "array": False, "value": 4},
                5: {"name": "REST_API", "type": 0, "array": False, "value": 5},
            }
        ),
    },
    {
        "name": "SectionPresetInfo",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "shelfId", "type": -8, "array": False, "value": 1},
                2: {"name": "templateId", "type": -8, "array": False, "value": 2},
                3: {"name": "templateName", "type": -6, "array": False, "value": 3},
            }
        ),
    },
    {
        "name": "VariableIdOrVariableOverrideId",
        "kind": 2,
        "fields": OrderedDict(
            {
                1: {"name": "variableId", "type": 96, "array": False, "value": 1},
                2: {"name": "variableOverrideId", "type": 97, "array": False, "value": 2},
            }
        ),
    },
]
{
    "name": "Message",
    "kind": 2,
    "fields": OrderedDict(
        {
            1: {"name": "type", "type": 0, "array": False, "value": 1},
            2: {"name": "sessionID", "type": -4, "array": False, "value": 2},
            3: {"name": "ackID", "type": -4, "array": False, "value": 3},
            4: {"name": "nodeChanges", "type": 152, "array": True, "value": 4},
            5: {"name": "userChanges", "type": 245, "array": True, "value": 5},
            32: {
                "name": "interactiveSlideElementChange",
                "type": 246,
                "array": False,
                "value": 32,
            },
            6: {"name": "blobs", "type": 67, "array": True, "value": 6},
            30: {"name": "blobBaseIndex", "type": -4, "array": False, "value": 30},
            7: {"name": "signalName", "type": -6, "array": False, "value": 7},
            8: {"name": "access", "type": 2, "array": False, "value": 8},
            9: {"name": "styleSetName", "type": -6, "array": False, "value": 9},
            10: {"name": "styleSetType", "type": 31, "array": False, "value": 10},
            11: {"name": "styleSetContentType", "type": 32, "array": False, "value": 11},
            12: {"name": "pasteID", "type": -3, "array": False, "value": 12},
            13: {"name": "pasteOffset", "type": 49, "array": False, "value": 13},
            14: {"name": "pasteFileKey", "type": -6, "array": False, "value": 14},
            15: {"name": "signalPayload", "type": -6, "array": False, "value": 15},
            16: {"name": "sceneGraphQueries", "type": 248, "array": True, "value": 16},
            17: {"name": "nodeChangesMetadata", "type": 249, "array": False, "value": 17},
            18: {"name": "fileVersion", "type": -4, "array": False, "value": 18},
            19: {
                "name": "pasteIsPartiallyOutsideEnclosingFrame",
                "type": -1,
                "array": False,
                "value": 19,
            },
            20: {"name": "pastePageId", "type": 47, "array": False, "value": 20},
            21: {"name": "isCut", "type": -1, "array": False, "value": 21},
            22: {"name": "localUndoStack", "type": 256, "array": True, "value": 22},
            23: {"name": "localRedoStack", "type": 256, "array": True, "value": 23},
            24: {"name": "broadcasts", "type": 255, "array": True, "value": 24},
            25: {"name": "reconnectSequenceNumber", "type": -4, "array": False, "value": 25},
            26: {"name": "pasteBranchSourceFileKey", "type": -6, "array": False, "value": 26},
            27: {"name": "pasteEditorType", "type": 147, "array": False, "value": 27},
            28: {"name": "postSyncActions", "type": -6, "array": False, "value": 28},
            29: {"name": "publishedAssetGuids", "type": 47, "array": True, "value": 29},
            31: {"name": "dirtyFromInitialLoad", "type": -1, "array": False, "value": 31},
        }
    ),
}
