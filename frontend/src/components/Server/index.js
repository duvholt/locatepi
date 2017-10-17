import React from 'react';
import PropTypes from 'prop-types';
import css from './Server.css';

const Server = ({ name, ip, lastUpdate }) => (
  <div className={css.component}>
    <div className={css.name}>{ name }</div>
    <div className={css.content}>
      <div className={css.ip}>{ ip }</div>
      <div className={css.date}>Last update: 2017-10-10 13:44</div>
    </div>
  </div>
);

Server.propTypes = {
  name: PropTypes.string.isRequired,
  ip: PropTypes.string.isRequired,
  lastUpdate: PropTypes.instanceOf(Date).isRequired,
}

export default Server;
