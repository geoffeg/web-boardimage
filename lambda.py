#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# web-boardimage is an HTTP service that renders chess board images.
# Copyright (C) 2016-2017 Niklas Fiekas <niklas.fiekas@backscattering.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""An HTTP service that renders chess board images"""

import chess
import chess.svg
import cairosvg
import re

def render(event, context):
    coords = event['pathParameters']['coords']
    flipped= event['pathParameters']['flipped']
    check = event['pathParameters']['check']
    size = event['pathParameters']['size']
    lastMove = event['pathParameters']['lastMove']
    orientation = event['pathParameters']['orientation']

    svg_data = chess.svg.board(board, coordinates=coords, flipped=flipped, lastmove=lastmove, check=check, size=size, style=None)
    png_data = cairosvg.svg2png(bytestring=svg_data)
    return aiohttp.web.Response(body=png_data, content_type="image/png")
