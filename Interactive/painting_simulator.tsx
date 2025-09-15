import React, { useState, useRef, useEffect } from 'react';

const COLORS = [
  '#FF0000', '#FF8800', '#FFFF00', '#88FF00', '#00FF00', '#00FF88',
  '#00FFFF', '#0088FF', '#0000FF', '#8800FF', '#FF00FF', '#FF0088',
  '#000000', '#444444', '#888888', '#CCCCCC', '#FFFFFF', '#8B4513',
  '#FFA500', '#FFB6C1', '#98FB98', '#87CEEB', '#DDA0DD', '#F0E68C'
];

const BRUSH_SIZES = [2, 5, 10, 15, 20, 30];
const BRUSH_TYPES = [
  { name: 'Round', type: 'round' },
  { name: 'Square', type: 'square' },
  { name: 'Soft', type: 'soft' }
];

export default function PaintingSimulator() {
  const canvasRef = useRef(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [selectedColor, setSelectedColor] = useState('#FF0000');
  const [brushSize, setBrushSize] = useState(10);
  const [brushType, setBrushType] = useState('round');
  const [opacity, setOpacity] = useState(1);
  const [tool, setTool] = useState('brush'); // brush, eraser, eyedropper
  const [history, setHistory] = useState([]);
  const [historyIndex, setHistoryIndex] = useState(-1);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (canvas) {
      const ctx = canvas.getContext('2d');
      ctx.fillStyle = 'white';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      saveToHistory();
    }
  }, []);

  const saveToHistory = () => {
    const canvas = canvasRef.current;
    const dataURL = canvas.toDataURL();
    const newHistory = history.slice(0, historyIndex + 1);
    newHistory.push(dataURL);
    setHistory(newHistory);
    setHistoryIndex(newHistory.length - 1);
  };

  const undo = () => {
    if (historyIndex > 0) {
      const canvas = canvasRef.current;
      const ctx = canvas.getContext('2d');
      const img = new Image();
      img.onload = () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, 0, 0);
      };
      img.src = history[historyIndex - 1];
      setHistoryIndex(historyIndex - 1);
    }
  };

  const redo = () => {
    if (historyIndex < history.length - 1) {
      const canvas = canvasRef.current;
      const ctx = canvas.getContext('2d');
      const img = new Image();
      img.onload = () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, 0, 0);
      };
      img.src = history[historyIndex + 1];
      setHistoryIndex(historyIndex + 1);
    }
  };

  const getCoordinates = (e) => {
    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    return {
      x: e.clientX - rect.left,
      y: e.clientY - rect.top
    };
  };

  const startDrawing = (e) => {
    setIsDrawing(true);
    const coords = getCoordinates(e);
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');

    if (tool === 'eyedropper') {
      const imageData = ctx.getImageData(coords.x, coords.y, 1, 1);
      const pixel = imageData.data;
      const color = `rgb(${pixel[0]}, ${pixel[1]}, ${pixel[2]})`;
      setSelectedColor(rgbToHex(pixel[0], pixel[1], pixel[2]));
      return;
    }

    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.globalAlpha = opacity;
    
    if (tool === 'eraser') {
      ctx.globalCompositeOperation = 'destination-out';
    } else {
      ctx.globalCompositeOperation = 'source-over';
      ctx.strokeStyle = selectedColor;
      ctx.fillStyle = selectedColor;
    }
    
    ctx.lineWidth = brushSize;
    ctx.beginPath();
    ctx.moveTo(coords.x, coords.y);
  };

  const draw = (e) => {
    if (!isDrawing || tool === 'eyedropper') return;
    
    const coords = getCoordinates(e);
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    
    if (brushType === 'soft') {
      // Create gradient brush effect
      const gradient = ctx.createRadialGradient(coords.x, coords.y, 0, coords.x, coords.y, brushSize / 2);
      gradient.addColorStop(0, tool === 'eraser' ? 'rgba(0,0,0,1)' : selectedColor);
      gradient.addColorStop(1, 'rgba(0,0,0,0)');
      
      if (tool === 'eraser') {
        ctx.globalCompositeOperation = 'destination-out';
      } else {
        ctx.fillStyle = gradient;
        ctx.globalCompositeOperation = 'source-over';
      }
      
      ctx.beginPath();
      ctx.arc(coords.x, coords.y, brushSize / 2, 0, Math.PI * 2);
      ctx.fill();
    } else if (brushType === 'square') {
      ctx.fillRect(coords.x - brushSize/2, coords.y - brushSize/2, brushSize, brushSize);
    } else {
      ctx.lineTo(coords.x, coords.y);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(coords.x, coords.y);
    }
  };

  const stopDrawing = () => {
    if (isDrawing && tool !== 'eyedropper') {
      setIsDrawing(false);
      const canvas = canvasRef.current;
      const ctx = canvas.getContext('2d');
      ctx.beginPath();
      ctx.globalCompositeOperation = 'source-over';
      ctx.globalAlpha = 1;
      saveToHistory();
    }
    setIsDrawing(false);
  };

  const clearCanvas = () => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    saveToHistory();
  };

  const rgbToHex = (r, g, b) => {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
  };

  const downloadImage = () => {
    const canvas = canvasRef.current;
    const link = document.createElement('a');
    link.download = 'my-painting.png';
    link.href = canvas.toDataURL();
    link.click();
  };

  return (
    <div className="max-w-7xl mx-auto p-4 bg-gradient-to-br from-purple-50 to-pink-50 min-h-screen">
      <div className="text-center mb-6">
        <h1 className="text-4xl font-bold text-gray-800 mb-2">🎨 Digital Painting Studio</h1>
        <p className="text-gray-600">Create your masterpiece with digital brushes and colors!</p>
      </div>

      <div className="flex gap-6">
        {/* Toolbar */}
        <div className="bg-white rounded-xl shadow-lg p-4 w-80">
          {/* Tools */}
          <div className="mb-6">
            <h3 className="font-semibold text-gray-700 mb-3">Tools:</h3>
            <div className="flex gap-2">
              {[
                { name: 'Brush', icon: '🖌️', value: 'brush' },
                { name: 'Eraser', icon: '🧽', value: 'eraser' },
                { name: 'Eyedropper', icon: '💧', value: 'eyedropper' }
              ].map(t => (
                <button
                  key={t.value}
                  className={`px-4 py-2 rounded-lg transition-all ${
                    tool === t.value 
                      ? 'bg-blue-500 text-white shadow-lg' 
                      : 'bg-gray-100 hover:bg-gray-200'
                  }`}
                  onClick={() => setTool(t.value)}
                >
                  {t.icon} {t.name}
                </button>
              ))}
            </div>
          </div>

          {/* Color Palette */}
          <div className="mb-6">
            <h3 className="font-semibold text-gray-700 mb-3">Colors:</h3>
            <div className="grid grid-cols-6 gap-2 mb-3">
              {COLORS.map(color => (
                <button
                  key={color}
                  className={`w-8 h-8 rounded-lg border-2 transition-all hover:scale-110 ${
                    selectedColor === color ? 'border-gray-800 scale-110' : 'border-gray-300'
                  }`}
                  style={{ backgroundColor: color }}
                  onClick={() => setSelectedColor(color)}
                />
              ))}
            </div>
            <input
              type="color"
              value={selectedColor}
              onChange={(e) => setSelectedColor(e.target.value)}
              className="w-full h-10 rounded-lg border-2 border-gray-300"
            />
          </div>

          {/* Brush Settings */}
          <div className="mb-6">
            <h3 className="font-semibold text-gray-700 mb-3">Brush Settings:</h3>
            
            <div className="mb-4">
              <label className="block text-sm text-gray-600 mb-2">Brush Type:</label>
              <div className="flex gap-2">
                {BRUSH_TYPES.map(brush => (
                  <button
                    key={brush.type}
                    className={`px-3 py-1 rounded-lg text-sm transition-all ${
                      brushType === brush.type
                        ? 'bg-blue-500 text-white'
                        : 'bg-gray-100 hover:bg-gray-200'
                    }`}
                    onClick={() => setBrushType(brush.type)}
                  >
                    {brush.name}
                  </button>
                ))}
              </div>
            </div>

            <div className="mb-4">
              <label className="block text-sm text-gray-600 mb-2">Size: {brushSize}px</label>
              <input
                type="range"
                min="1"
                max="50"
                value={brushSize}
                onChange={(e) => setBrushSize(parseInt(e.target.value))}
                className="w-full"
              />
            </div>

            <div className="mb-4">
              <label className="block text-sm text-gray-600 mb-2">Opacity: {Math.round(opacity * 100)}%</label>
              <input
                type="range"
                min="0.1"
                max="1"
                step="0.1"
                value={opacity}
                onChange={(e) => setOpacity(parseFloat(e.target.value))}
                className="w-full"
              />
            </div>
          </div>

          {/* Actions */}
          <div className="space-y-2">
            <div className="flex gap-2">
              <button
                onClick={undo}
                disabled={historyIndex <= 0}
                className="px-4 py-2 bg-gray-500 text-white rounded-lg hover:bg-gray-600 disabled:opacity-50 disabled:cursor-not-allowed flex-1"
              >
                ↶ Undo
              </button>
              <button
                onClick={redo}
                disabled={historyIndex >= history.length - 1}
                className="px-4 py-2 bg-gray-500 text-white rounded-lg hover:bg-gray-600 disabled:opacity-50 disabled:cursor-not-allowed flex-1"
              >
                ↷ Redo
              </button>
            </div>
            <button
              onClick={clearCanvas}
              className="w-full px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600"
            >
              🧹 Clear Canvas
            </button>
            <button
              onClick={downloadImage}
              className="w-full px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600"
            >
              💾 Download
            </button>
          </div>
        </div>

        {/* Canvas */}
        <div className="flex-1">
          <div className="bg-white rounded-xl shadow-2xl p-4">
            <h3 className="text-xl font-semibold text-gray-700 mb-4">Canvas</h3>
            <div className="border-4 border-gray-300 rounded-lg overflow-hidden shadow-inner">
              <canvas
                ref={canvasRef}
                width={800}
                height={600}
                className={`block ${tool === 'eyedropper' ? 'cursor-crosshair' : 'cursor-none'}`}
                onMouseDown={startDrawing}
                onMouseMove={draw}
                onMouseUp={stopDrawing}
                onMouseLeave={stopDrawing}
                style={{ touchAction: 'none' }}
              />
            </div>
            
            {/* Canvas Info */}
            <div className="mt-4 text-sm text-gray-600 flex justify-between">
              <span>Current tool: {tool} | Size: {brushSize}px | Color: {selectedColor}</span>
              <span>800 × 600px</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}