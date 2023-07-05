import { EthereumProvider } from '@walletconnect/ethereum-provider';

const projectId = 'WalletConnectV2';
const chains = [1];
const showQrModal = true;
const methods = ['eth_sendTransaction', 'eth_signTransaction'];
const optionalMethods = ['eth_sign', 'personal_sign'];
const events = {
  connect: (error, payload) => {
    if (error) {
      throw error;
    }
    console.log('connect', payload);
  },
  session_update: (error, payload) => {
    if (error) {
      throw error;
    }
    console.log('session_update', payload);
  },
  disconnect: (error, payload) => {
    if (error) {
      throw error;
    }
    console.log('disconnect', payload);
  },
};

const provider = await EthereumProvider.init({
  projectId, // REQUIRED your projectId
  chains, // REQUIRED chain ids
  showQrModal, // REQUIRED set to "true" to use @walletconnect/modal
  methods, // REQUIRED ethereum methods
  optionalMethods, // OPTIONAL ethereum methods
  events, // REQUIRED ethereum events
});

document.addEventListener('DOMContentLoaded', function () {
  const connectButton = document.getElementById('connect-wallet');

  connectButton.addEventListener('click', async () => {
    try {
      await provider.enable();
    } catch (error) {
      console.error('Failed to enable provider', error);
    }
  });
});
