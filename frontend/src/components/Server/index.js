import React from 'react';
import { graphql, createFragmentContainer } from 'react-relay';
import formatRelative from 'date-fns/formatRelative';

import PropTypes from 'prop-types';
import classNames from 'classnames';
import css from './Server.css';

const Server = ({ server }) => {
  const offline = false;
  const { name, ip, lastUpdate } = server;
  const relativeTime = formatRelative(new Date(lastUpdate), new Date());
  return (
    <div className={css.component}>
      <div
        className={classNames(
          css.name, {
            [css.offline]: offline,
          }
        )}
      >
        { name }
      </div>
      <div className={css.content}>
        <div className={css.ip}>{ ip }</div>
        <div className={css.date}>{lastUpdate && `Last update: ${relativeTime}` }</div>
      </div>
    </div>
  );
}

Server.propTypes = {
  server: PropTypes.shape({
    name: PropTypes.string.isRequired,
    ip: PropTypes.string,
    lastUpdate: PropTypes.string,
  }).isRequired,
}

export default createFragmentContainer(
  Server,
  graphql`
    fragment Server_server on Server {
      ip,
      name,
      lastUpdate,
    }
  `,
);
