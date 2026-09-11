using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Visualizador
{
    public partial class ViewerForm : Form
    {
        public ViewerForm()
        {
            InitializeComponent();
        }

        private void btnSelectPicture_Click(object sender, EventArgs e)
        {
            if (ofdSelectPicture.ShowDialog() == DialogResult.OK)
            {
                picShowPicture.Image = Image.FromFile(ofdSelectPicture.FileName);
                this.Text = String.Concat("Picture Viewer(" + ofdSelectPicture.FileName + ")");
            }
        }

        private void btnQuit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void btnEnlarge_Click(object sender, EventArgs e)
        {
            this.Width += 20;
            this.Height += 20;
        }

        private void btnShrink_Click(object sender, EventArgs e)
        {
            this.Width -= 20;
            this.Height -= 20;
        }

        private void btnDrawBorder_Click(object sender, EventArgs e)
        {
            Graphics objGraphics = null;
            objGraphics = this.CreateGraphics();
            objGraphics.Clear(SystemColors.Control);

            objGraphics.DrawRectangle(
                Pens.Blue,
                picShowPicture.Left - 1,
                picShowPicture.Top - 1,
                picShowPicture.Width + 1,
                picShowPicture.Height + 1
            );

            objGraphics.Dispose();
        }

        private void picShowPicture_MouseMove(object sender, MouseEventArgs e)
        {
            lblX.Text = "X: " + e.X.ToString();
            lblY.Text = "Y: " + e.Y.ToString();
        }

        private void picShowPicture_MouseLeave(object sender, EventArgs e)
        {
            lblX.Text = "";
            lblY.Text = "";
        }

        private void ViewerForm_Load(object sender, EventArgs e)
        {
            lblX.Text = "";
            lblY.Text = "";
        }

        private void btnOptions_Click(object sender, EventArgs e)
        {
            OptionsForm frmOptionsDialog = new OptionsForm();
            frmOptionsDialog.Show();
        }
    }
}
