import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ItemList } from './App'; // Import the ItemList component

describe('ItemList Component', () => {
  const sampleItems = ['Item 1', 'Item 2', 'Item 3'];
  
  test('renders correct number of items', () => {
    render(<ItemList items={sampleItems} />);
    const listItems = screen.getAllByTestId('list-item');
    expect(listItems).toHaveLength(sampleItems.length);
  });
  
  test('renders empty list when no items provided', () => {
    render(<ItemList items={[]} />);
    const listItems = screen.queryAllByTestId('list-item');
    expect(listItems).toHaveLength(0);
  });
  
  test('renders correct item content', () => {
    render(<ItemList items={sampleItems} />);
    sampleItems.forEach(item => {
      expect(screen.getByText(item)).toBeInTheDocument();
    });
  });
});