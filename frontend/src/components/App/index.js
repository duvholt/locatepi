import React from 'react';
import css from './App.css';
import Servers from '../Servers';

const App = () => (
  <div>
    <div className={css.component}>
      <div className={css.header}>
        <h2>Locatepi</h2>
      </div>
      <div className={css.content}>
        <Servers />
      </div>
    </div>
    <div className={css.backgroundCircle} />
  </div>
);

export default App;
