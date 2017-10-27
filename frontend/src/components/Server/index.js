import React from 'react';
import { graphql, createFragmentContainer } from 'react-relay';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import css from './Server.css';

const Server = ({ server }) => {
  const offline = false;
  const { name, ip } = server;
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
        <div className={css.date}>Last update: 2017-10-10 13:44</div>
      </div>
    </div>
  );
}

Server.defaultProps = {
  offline: false,
}

Server.propTypes = {
  name: PropTypes.string.isRequired,
  ip: PropTypes.string.isRequired,
  lastUpdate: PropTypes.instanceOf(Date).isRequired,
  offline: PropTypes.bool,
}

export default createFragmentContainer(
  Server,
  graphql`
    fragment Server_server on Server {
      ip,
      name,
    }
  `,
);
