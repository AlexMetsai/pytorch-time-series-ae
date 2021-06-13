import torch
from torch import nn


class ConvAutoencoder(nn.Module):
    def __init__(self, feat_dim=1, enc_dim=10, channels=1, strides=1):
        
        super().__init__()
       
        #Encoder
        self.conv1 = nn.Conv1d(channels, enc_dim, 7, strides, padding=0)  
        self.dropout = nn.Dropout(0.2)
        
        #Decoder
        self.t_conv1 = nn.ConvTranspose1d(enc_dim, 1, 7, strides, padding=0)
        self.t_conv2 = nn.ConvTranspose1d(1, 1, 1, strides, padding=0)
    
    def forward(self, x):
        
        #Encoder
        x = self.conv1(x)
        x = self.dropout(x)
        
        # Decoder
        x =  self.t_conv1(x)
        x =  self.t_conv2(x)
        
        return x


if __name__ == "__main__":
    
    model = ConvAutoencoder(10)
    
    # batch, seq_len, num_feat
    a = torch.zeros((1, 1, 100))
    out = model(a)
    print(a.shape, out.shape)
    
    a = torch.zeros((1, 1, 153))
    out = model(a)
    print(a.shape, out.shape)
