import React from 'react';
import Server from '../Server';
import css from './Servers.css';

const Servers = () => (
  <div className={css.component}>
    <Server name="Onlinekontoret Pi Inngang" ip="129.241.105.255" lastUpdate={new Date()} />
    <Server name="Onlinekontoret Pi Kjøleskap" ip="129.241.105.255" lastUpdate={new Date()} />
  </div>
);

export default Servers;
