import React, { useState, useRef } from 'react';

const COLORS = [
  { name: 'Red', value: '#DC2626' },
  { name: 'Blue', value: '#2563EB' },
  { name: 'Green', value: '#16A34A' },
  { name: 'Yellow', value: '#EAB308' },
  { name: 'Orange', value: '#EA580C' },
  { name: 'Purple', value: '#9333EA' },
  { name: 'Pink', value: '#EC4899' },
  { name: 'White', value: '#F8FAFC' },
  { name: 'Gray', value: '#64748B' },
  { name: 'Black', value: '#1E293B' }
];

const GRID_SIZE = 16;

export default function LegoBuilder() {
  const [selectedColor, setSelectedColor] = useState(COLORS[0].value);
  const [grid, setGrid] = useState(() => 
    Array(GRID_SIZE).fill(null).map(() => Array(GRID_SIZE).fill(null))
  );
  const [isErasing, setIsErasing] = useState(false);
  const [isDragging, setIsDragging] = useState(false);

  const handleCellClick = (row, col) => {
    const newGrid = [...grid];
    if (isErasing) {
      newGrid[row][col] = null;
    } else {
      newGrid[row][col] = selectedColor;
    }
    setGrid(newGrid);
  };

  const handleMouseEnter = (row, col) => {
    if (isDragging) {
      const newGrid = [...grid];
      if (isErasing) {
        newGrid[row][col] = null;
      } else {
        newGrid[row][col] = selectedColor;
      }
      setGrid(newGrid);
    }
  };

  const clearAll = () => {
    setGrid(Array(GRID_SIZE).fill(null).map(() => Array(GRID_SIZE).fill(null)));
  };

  const LegoBlock = ({ color, onClick, onMouseEnter }) => (
    <div
      className={`w-8 h-8 border-2 border-gray-300 cursor-pointer transition-all duration-150 hover:scale-110 relative ${
        color ? 'shadow-lg' : 'bg-green-100'
      }`}
      style={{
        backgroundColor: color || '#dcfce7',
        borderColor: color ? '#000' : '#d1d5db'
      }}
      onClick={onClick}
      onMouseEnter={onMouseEnter}
    >
      {color && (
        <>
          {/* LEGO studs */}
          <div className="absolute inset-1 grid grid-cols-2 gap-px">
            {[...Array(4)].map((_, i) => (
              <div
                key={i}
                className="rounded-full"
                style={{
                  backgroundColor: color,
                  filter: 'brightness(1.3)',
                  boxShadow: 'inset 0 1px 2px rgba(0,0,0,0.3)'
                }}
              />
            ))}
          </div>
        </>
      )}
    </div>
  );

  return (
    <div className="max-w-6xl mx-auto p-6 bg-gradient-to-br from-blue-50 to-green-50 min-h-screen">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800 mb-2">🧱 LEGO Builder Simulator</h1>
        <p className="text-gray-600">Click and drag to build your LEGO masterpiece!</p>
      </div>

      {/* Controls */}
      <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
        <div className="mb-6">
          <h3 className="text-lg font-semibold text-gray-700 mb-3">Choose Your Brick Color:</h3>
          <div className="flex flex-wrap gap-2">
            {COLORS.map((color) => (
              <button
                key={color.name}
                className={`w-12 h-12 rounded-lg border-4 transition-all duration-200 hover:scale-110 ${
                  selectedColor === color.value ? 'border-gray-800 scale-110' : 'border-gray-300'
                }`}
                style={{ backgroundColor: color.value }}
                onClick={() => {
                  setSelectedColor(color.value);
                  setIsErasing(false);
                }}
                title={color.name}
              />
            ))}
          </div>
        </div>

        <div className="flex gap-4">
          <button
            className={`px-6 py-2 rounded-lg font-semibold transition-all duration-200 ${
              isErasing
                ? 'bg-red-500 text-white shadow-lg'
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            }`}
            onClick={() => setIsErasing(!isErasing)}
          >
            🗑️ {isErasing ? 'Erasing Mode' : 'Build Mode'}
          </button>
          <button
            className="px-6 py-2 bg-orange-500 text-white rounded-lg font-semibold hover:bg-orange-600 transition-all duration-200 shadow-lg hover:shadow-xl"
            onClick={clearAll}
          >
            🧹 Clear All
          </button>
        </div>
      </div>

      {/* LEGO Baseplate */}
      <div className="bg-white rounded-xl shadow-2xl p-8">
        <div className="mb-4">
          <h3 className="text-xl font-semibold text-gray-700">Building Baseplate</h3>
          <p className="text-sm text-gray-500 mt-1">
            {isErasing ? 'Click or drag to remove bricks' : 'Click or drag to place bricks'}
          </p>
        </div>
        
        <div 
          className="inline-block border-4 border-green-600 rounded-lg p-2 bg-green-200"
          onMouseLeave={() => setIsDragging(false)}
        >
          <div className="grid gap-1" style={{ gridTemplateColumns: `repeat(${GRID_SIZE}, 1fr)` }}>
            {grid.map((row, rowIndex) =>
              row.map((cell, colIndex) => (
                <LegoBlock
                  key={`${rowIndex}-${colIndex}`}
                  color={cell}
                  onClick={() => handleCellClick(rowIndex, colIndex)}
                  onMouseEnter={() => handleMouseEnter(rowIndex, colIndex)}
                />
              ))
            )}
          </div>
        </div>

        <div className="mt-4 text-center">
          <button
            className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors"
            onMouseDown={() => setIsDragging(true)}
            onMouseUp={() => setIsDragging(false)}
          >
            Hold to Enable Drag Mode
          </button>
        </div>
      </div>

      {/* Stats */}
      <div className="mt-6 bg-white rounded-xl shadow-lg p-4">
        <h4 className="font-semibold text-gray-700 mb-2">Build Statistics:</h4>
        <p className="text-gray-600">
          Total Bricks: {grid.flat().filter(cell => cell !== null).length} / {GRID_SIZE * GRID_SIZE}
        </p>
      </div>
    </div>
  );
}