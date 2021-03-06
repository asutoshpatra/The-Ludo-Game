{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Color:\n",
    "\n",
    "    GREEN = '#008000'\n",
    "    RED = '#FF0000'\n",
    "    YELLOW = '#FFFF00'\n",
    "    BLUE = '#0000FF'\n",
    "    DEFAULT = '#FFFFFF'\n",
    "    INDIGO = '#4B0082'\n",
    "    AQUA = '#00FFFF'\n",
    "\n",
    "\n",
    "class Board:\n",
    "\n",
    "    SQUARE_SIZE = 40\n",
    "    PANEL_WIDTH = 600\n",
    "    PANEL_HEIGHT = 640\n",
    "    BOARD_WIDTH = 640\n",
    "    BOARD_HEIGHT = 640\n",
    "    POINTS = [(0, 0), (0, 1), (1, 0), (1, 1)]\n",
    "    POSITIVE_V = [(6, 2), (8, 1), (6, 13), (8, 12)]\n",
    "    POSITIVE_H = [(1, 6), (2, 8), (13, 8), (12, 6)]\n",
    "\n",
    "\n",
    "class Text:\n",
    "\n",
    "    MADE_BY = 'Made By: TEAM NO. 18'\n",
    "    HEADER =  'THE LUDO GAME'\n",
    "\n",
    "\n",
    "class Path:\n",
    "\n",
    "    def __init__(self):\n",
    "\n",
    "        self.green_path = []\n",
    "        self.red_path = []\n",
    "        self.blue_path = []\n",
    "        self.yellow_path = []\n",
    "        self.gx = None\n",
    "        self.gy = None \n",
    "        self.ry = None\n",
    "        self.by = None\n",
    "        self.count = None\n",
    "\n",
    "    def update_coordinates(self, gx, gy, ry, by, count):\n",
    "\n",
    "        self.gx = gx\n",
    "        self.gy = gy\n",
    "        self.ry = ry\n",
    "        self.by = by\n",
    "        self.count = count\n",
    "\n",
    "    def start_populating(self):\n",
    "\n",
    "        #1\n",
    "        self.update_coordinates(60, 260, 540, 340, 5)\n",
    "        self.direct(pow_index=0, direction='right')\n",
    "        #2\n",
    "        self.update_coordinates(260, 220, 340, 380, 5)\n",
    "        self.direct(pow_index=3, direction='up')\n",
    "        #3\n",
    "        self.update_coordinates(260, 20, 340, 580, 3)\n",
    "        self.direct(direction='right') \n",
    "        #4\n",
    "        self.update_coordinates(340, 60, 260, 540, 5)\n",
    "        self.direct(pow_index=0, direction='down')\n",
    "        #5\n",
    "        self.update_coordinates(380, 260, 220, 340, 5)\n",
    "        self.direct(pow_index=3, direction='right')\n",
    "        #6\n",
    "        self.update_coordinates(580, 260, 20, 340, 3)\n",
    "        self.direct(direction='down')\n",
    "        #7\n",
    "        self.update_coordinates(540, 340, 60, 260, 5)\n",
    "        self.direct(pow_index=0, direction='left')\n",
    "        #8\n",
    "        self.update_coordinates(340, 380, 260, 220, 5)\n",
    "        self.direct(pow_index=3, direction='down')\n",
    "        #9\n",
    "        self.update_coordinates(340, 580, 260, 20, 3)\n",
    "        self.direct(direction='left')\n",
    "        #10\n",
    "        self.update_coordinates(260, 540, 340, 60, 5)\n",
    "        self.direct(pow_index=0, direction='up')\n",
    "        #11\n",
    "        self.update_coordinates(220, 340, 380, 260, 6)\n",
    "        self.direct(pow_index=3, direction='left')\n",
    "        #12\n",
    "        self.update_coordinates(20, 300, 580, 300, 7)\n",
    "        self.direct(direction='right')\n",
    "\n",
    "    def direct_horizontal(self, k, pow_index = -1):\n",
    "\n",
    "        for i in range(self.count):\n",
    "            if i == pow_index:\n",
    "                p = 1\n",
    "            else:\n",
    "                p = 0\n",
    "            self.green_path.append((self.gx  +  k*i*Board.SQUARE_SIZE, self.gy, p))\n",
    "            self.red_path.append((self.gy, self.ry  -  k*i*Board.SQUARE_SIZE, p))\n",
    "            self.blue_path.append((self.ry - k*i*Board.SQUARE_SIZE, self.by, p))\n",
    "            self.yellow_path.append((self.by, self.gx + k*i*Board.SQUARE_SIZE, p))\n",
    "\n",
    "    def direct_vertical(self, k, pow_index = -1):\n",
    "\n",
    "        for i in range(self.count):\n",
    "            if i == pow_index:\n",
    "                p = 1\n",
    "            else:\n",
    "                p = 0\n",
    "            self.green_path.append((self.gx, self.gy - k*i*Board.SQUARE_SIZE, p))\n",
    "            self.red_path.append((self.gy - k*i*Board.SQUARE_SIZE,self.ry, p))\n",
    "            self.blue_path.append((self.ry, self.by + k*i*Board.SQUARE_SIZE, p))\n",
    "            self.yellow_path.append((self.by + k*i*Board.SQUARE_SIZE, self.gx, p))\n",
    "\n",
    "\n",
    "    def direct(self, direction, pow_index = -1):\n",
    "        if direction=='right':\n",
    "            self.direct_horizontal(1, pow_index=pow_index)\n",
    "        elif direction=='left':\n",
    "            self.direct_horizontal(-1, pow_index=pow_index)\n",
    "        elif direction=='down':\n",
    "            self.direct_vertical(-1, pow_index=pow_index)\n",
    "        else:\n",
    "            self.direct_vertical(1, pow_index=pow_index)\n",
    "\n",
    "path = Path()\n",
    "path.start_populating()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
