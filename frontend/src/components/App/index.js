import React from 'react';
import css from './App.css';
import Server from '../Server';

const App = () => (
  <div>
    <div className={css.component}>
      <div className={css.header}>
        <h2>Surveillance Center</h2>
      </div>
      <div className={css.content}>
        <Server name="Onlinekontoret Pi Inngang" ip="129.241.105.255" lastUpdate={new Date()} />
        <Server name="Onlinekontoret Pi Kjøleskap" ip="129.241.105.255" lastUpdate={new Date()} />
      </div>
    </div>
    <div className={css.backgroundCircle} />
  </div>
);

export default App;
